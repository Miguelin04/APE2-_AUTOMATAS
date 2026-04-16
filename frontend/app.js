const API_URL = "http://127.0.0.1:8000/api";

// Navegación (Tabs)
document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        // Quitar active de todos los btns
        document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
        // Poner active al actual
        e.target.classList.add('active');

        // Ocultar todas las sections
        document.querySelectorAll('.tab-pane').forEach(sec => sec.classList.remove('active'));
        // Mostrar la correspondiente
        const targetId = e.target.getAttribute('data-target');
        document.getElementById(targetId).classList.add('active');
        
        // Limpiar resultados
        document.getElementById('resultado_box').innerHTML = '<span class="placeholder">Selecciona una operación y presiona el botón.</span>';
    });
});

// Funciones de utilidad para parsers
function parseList(str) {
    if (!str.trim()) return [""];
    return str.split(',').map(s => s.trim());
}

function displayArray(arr) {
    if (arr.length === 0) return 'Ø (Vacío)';
    return `<div class="list-results">` + arr.map(a => `<span class="pill">${a === "" ? "ε" : a}</span>`).join('') + `</div>`;
}

// Llamadas a la API
async function apiCall(endpoint, payload) {
    try {
        const res = await fetch(`${API_URL}/${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        return data.resultado;
    } catch (err) {
        console.error(err);
        return "Error en la conexión con el servidor.";
    }
}

// Controladores de Eventos
async function executeGenerar() {
    const alfabeto = parseList(document.getElementById('gen_alfabeto').value);
    const maxLen = parseInt(document.getElementById('gen_max_len').value);
    const res = await apiCall('generar_cadenas', { alfabeto, max_len: maxLen });
    document.getElementById('resultado_box').innerHTML = displayArray(res);
}

async function executePertenencia() {
    const cadena = document.getElementById('pert_cadena').value.trim();
    const lenguaje = parseList(document.getElementById('pert_lenguaje').value);
    const res = await apiCall('pertenece', { cadena, lenguaje });
    document.getElementById('resultado_box').innerHTML = res ? '<span style="color:#10b981;font-weight:bold;">¡VERDADERO!</span> La cadena pertenece al lenguaje.' : '<span style="color:#ef4444;font-weight:bold;">FALSO.</span> La cadena no pertenece al lenguaje.';
}

async function executeUnion() {
    const l1 = parseList(document.getElementById('uni_l1').value);
    const l2 = parseList(document.getElementById('uni_l2').value);
    const res = await apiCall('union', { l1, l2 });
    document.getElementById('resultado_box').innerHTML = displayArray(res);
}

async function executeConcatenacion() {
    const l1 = parseList(document.getElementById('con_l1').value);
    const l2 = parseList(document.getElementById('con_l2').value);
    const res = await apiCall('concatenacion', { l1, l2 });
    document.getElementById('resultado_box').innerHTML = displayArray(res);
}

async function executeKleeneStar() {
    const l = parseList(document.getElementById('ks_l').value);
    const iter = parseInt(document.getElementById('ks_iter').value);
    const res = await apiCall('kleene_star', { l, max_iter: iter });
    document.getElementById('resultado_box').innerHTML = displayArray(res);
}

async function executeKleenePlus() {
    const l = parseList(document.getElementById('kp_l').value);
    const iter = parseInt(document.getElementById('kp_iter').value);
    const res = await apiCall('kleene_plus', { l, max_iter: iter });
    document.getElementById('resultado_box').innerHTML = displayArray(res);
}

async function executeCrecimiento() {
    const l = parseList(document.getElementById('cre_l').value);
    const res = await apiCall('analizar_crecimiento', { l });
    if(Array.isArray(res)) {
        let text = "<pre>";
        for(let item of res) {
            text += `Iteración: ${item.iteracion}  ->  Cantidad de elementos: ${item.cantidad}\n`;
        }
        text += "</pre>";
        document.getElementById('resultado_box').innerHTML = text;
    } else {
        document.getElementById('resultado_box').innerHTML = res;
    }
}
