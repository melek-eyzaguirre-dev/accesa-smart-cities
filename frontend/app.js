/**
 * ACCESA Smart Cities - Frontend Application
 * ============================================
 * Conecta el dashboard con la API Flask
 */

const API_BASE = window.location.origin;

// ===== STATE =====
const state = {
    connected: false,
    tokenCreated: false,
    tokenId: null,
    userAgents: [],
    serviceAgents: [],
    transactions: [],
    txCount: 0,
};

// ===== DOM ELEMENTS =====
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

// ===== TOAST NOTIFICATIONS =====
function showToast(message, type = 'info') {
    const container = $('#toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast toast--${type}`;
    const icons = { success: '✅', error: '❌', info: 'ℹ️' };
    toast.innerHTML = `<span>${icons[type] || 'ℹ️'}</span><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
        toast.classList.add('toast--exit');
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// ===== API CALLS =====
async function apiCall(endpoint, method = 'GET', body = null) {
    try {
        const options = {
            method,
            headers: { 'Content-Type': 'application/json' },
        };
        if (body) options.body = JSON.stringify(body);

        const response = await fetch(`${API_BASE}${endpoint}`, options);
        const data = await response.json();

        if (!response.ok) throw new Error(data.error || 'Error en la API');
        return data;
    } catch (error) {
        console.error(`API Error [${endpoint}]:`, error);
        throw error;
    }
}

// ===== CONNECTION =====
async function checkConnection() {
    try {
        const data = await apiCall('/health');
        state.connected = data.status === 'healthy';
        updateConnectionStatus(true, data.network, data.account_id);
        showToast(`Conectado a Hedera ${data.network.toUpperCase()}`, 'success');
        await refreshStats();
        return true;
    } catch (error) {
        state.connected = false;
        updateConnectionStatus(false);
        showToast('No se pudo conectar. ¿Está corriendo la API? (python api/app.py)', 'error');
        return false;
    }
}

function updateConnectionStatus(connected, network = '', accountId = '') {
    const statusEl = $('#connectionStatus');
    const dot = statusEl.querySelector('.status__dot');
    const text = statusEl.querySelector('.status__text');

    dot.className = `status__dot status__dot--${connected ? 'connected' : 'disconnected'}`;
    text.textContent = connected
        ? `${network} · ${accountId}`
        : 'Desconectado';
}

// ===== STATS =====
async function refreshStats() {
    try {
        // Balance
        const balance = await apiCall('/account/balance');
        $('#hbarBalance').textContent = `${parseFloat(balance.hbar_balance).toFixed(2)}`;
        animateValue($('#hbarBalance'));

        // Marketplace stats
        const stats = await apiCall('/marketplace/stats');
        $('#usersCount').textContent = stats.users_registered;
        $('#servicesCount').textContent = stats.services_registered;
        animateValue($('#usersCount'));
        animateValue($('#servicesCount'));
    } catch (error) {
        console.log('Stats refresh error (API may not be running)');
    }
}

function animateValue(el) {
    el.style.transform = 'scale(1.15)';
    el.style.transition = 'transform 0.3s ease';
    setTimeout(() => {
        el.style.transform = 'scale(1)';
    }, 300);
}

// ===== TOKEN =====
async function createToken() {
    const btn = $('#btnCreateToken');
    const originalText = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<span class="btn__spinner"></span> Creando en Hedera...';

    try {
        const result = await apiCall('/token/create', 'POST', {
            initial_supply: 1000000,
            decimals: 2,
        });

        state.tokenCreated = true;
        state.tokenId = result.token_id;

        // Update UI
        $('#tokenStatus').textContent = state.tokenId;
        animateValue($('#tokenStatus'));

        const tokenResult = $('#tokenResult');
        tokenResult.classList.remove('hidden');
        $('#tokenIdDisplay').textContent = state.tokenId;
        $('#tokenHashscanLink').href = `https://hashscan.io/testnet/token/${state.tokenId}`;

        showToast(`Token ACCESA creado: ${state.tokenId}`, 'success');
    } catch (error) {
        showToast(`Error creando token: ${error.message}`, 'error');
    } finally {
        btn.disabled = false;
        btn.innerHTML = originalText;
    }
}

// ===== USER AGENTS =====
async function createUserAgent(e) {
    e.preventDefault();
    const form = e.target;
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<span class="btn__spinner"></span> Creando...';

    const userId = $('#userId').value.trim().replace(/\s+/g, '_');
    const needs = $('#userNeeds').value;
    const budget = parseInt($('#userBudget').value);

    try {
        const result = await apiCall('/agent/user/create', 'POST', {
            user_id: userId,
            accessibility_needs: [needs],
            initial_budget: budget,
        });

        state.userAgents.push(result);
        renderUserAgent(result);
        updateTxUserSelect();
        await refreshStats();

        form.reset();
        $('#userBudget').value = 500;
        showToast(`Agente "${userId}" creado con ${budget} ACCESA`, 'success');
    } catch (error) {
        showToast(`Error: ${error.message}`, 'error');
    } finally {
        btn.disabled = false;
        btn.innerHTML = originalText;
    }
}

function renderUserAgent(agent) {
    const list = $('#userAgentsList');
    const needsIcons = {
        visual_impairment: '👁️',
        hearing_impairment: '👂',
        mobility: '🦽',
    };
    const needsLabels = {
        visual_impairment: 'Baja visión',
        hearing_impairment: 'Disc. auditiva',
        mobility: 'Movilidad reducida',
    };
    const need = agent.needs?.[0] || 'visual_impairment';

    const item = document.createElement('div');
    item.className = 'agent-item';
    item.setAttribute('role', 'listitem');
    item.innerHTML = `
        <span class="agent-item__emoji">${needsIcons[need] || '👤'}</span>
        <div class="agent-item__info">
            <div class="agent-item__name">${agent.agent_id}</div>
            <div class="agent-item__detail">${needsLabels[need] || need}</div>
        </div>
        <span class="agent-item__badge agent-item__badge--budget">${agent.budget} ACCESA</span>
    `;
    list.appendChild(item);
}

// ===== SERVICE AGENTS =====
async function createServiceAgent(e) {
    e.preventDefault();
    const form = e.target;
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<span class="btn__spinner"></span> Creando...';

    const buildingName = $('#buildingName').value.trim();

    try {
        const result = await apiCall('/agent/service/create', 'POST', {
            building_name: buildingName,
        });

        state.serviceAgents.push(result);
        renderServiceAgent(result);
        await refreshStats();

        form.reset();
        showToast(`Servicio "${buildingName}" registrado`, 'success');
    } catch (error) {
        showToast(`Error: ${error.message}`, 'error');
    } finally {
        btn.disabled = false;
        btn.innerHTML = originalText;
    }
}

function renderServiceAgent(agent) {
    const list = $('#serviceAgentsList');
    const serviceCount = agent.services?.length || 3;

    const item = document.createElement('div');
    item.className = 'agent-item';
    item.setAttribute('role', 'listitem');
    item.innerHTML = `
        <span class="agent-item__emoji">🏛️</span>
        <div class="agent-item__info">
            <div class="agent-item__name">${agent.agent_id}</div>
            <div class="agent-item__detail">${serviceCount} servicios disponibles</div>
        </div>
    `;
    list.appendChild(item);
}

// ===== TRANSACTIONS =====
function updateTxUserSelect() {
    const select = $('#txUserId');
    select.innerHTML = '<option value="">-- Selecciona usuario --</option>';
    state.userAgents.forEach((agent) => {
        const option = document.createElement('option');
        option.value = agent.agent_id;
        option.textContent = `${agent.agent_id} (${agent.budget} ACCESA)`;
        select.appendChild(option);
    });
}

async function executeTransaction(e) {
    e.preventDefault();
    const userId = $('#txUserId').value;
    const serviceType = $('#txServiceType').value;

    if (!userId) {
        showToast('Selecciona un usuario primero', 'error');
        return;
    }

    if (state.serviceAgents.length === 0) {
        showToast('Crea al menos un servicio primero', 'error');
        return;
    }

    const btn = $('#btnExecuteTx');
    const originalText = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<span class="btn__spinner"></span> Procesando en Hedera...';

    // Show animation
    const animEl = $('#txAnimation');
    animEl.classList.remove('hidden');

    const serviceLabels = {
        visual_impairment: 'Guía de Voz',
        hearing_impairment: 'Videos Lengua de Señas',
        mobility: 'Mapa Accesible',
    };

    $('#txAnimUser').textContent = userId;
    $('#txAnimService').textContent = serviceLabels[serviceType];

    try {
        const result = await apiCall('/agent/transaction', 'POST', {
            user_id: userId,
            service_type: serviceType,
        });

        state.txCount++;

        if (result.status === 'success') {
            const cost = result.service?.price || '?';
            $('#txAnimAmount').textContent = `${cost} ACCESA`;

            addTransactionRow({
                num: state.txCount,
                user: userId,
                service: serviceLabels[serviceType],
                cost: `${cost} ACCESA`,
                status: 'success',
            });

            showToast(`Transacción exitosa: ${cost} ACCESA pagados`, 'success');
        } else {
            addTransactionRow({
                num: state.txCount,
                user: userId,
                service: serviceLabels[serviceType],
                cost: '—',
                status: 'rejected',
            });
            showToast(`Transacción rechazada: ${result.reason || 'Sin fondos o sin necesidad'}`, 'info');
        }

        await refreshStats();
    } catch (error) {
        showToast(`Error: ${error.message}`, 'error');
        animEl.classList.add('hidden');
    } finally {
        btn.disabled = false;
        btn.innerHTML = originalText;
    }
}

function addTransactionRow({ num, user, service, cost, status }) {
    const tbody = $('#txHistoryBody');

    // Remove empty state
    const emptyRow = tbody.querySelector('.table__empty');
    if (emptyRow) emptyRow.remove();

    const row = document.createElement('tr');
    row.className = 'table__row-new';

    const statusClass = status === 'success' ? 'table__status--success' : 'table__status--rejected';
    const statusLabel = status === 'success' ? '✅ Éxito' : '❌ Rechazada';

    row.innerHTML = `
        <td>${num}</td>
        <td>${user}</td>
        <td>${service}</td>
        <td><strong>${cost}</strong></td>
        <td><span class="table__status ${statusClass}">${statusLabel}</span></td>
    `;

    tbody.insertBefore(row, tbody.firstChild);
}

// ===== DEMO MODE =====
async function runDemo() {
    if (!state.connected) {
        const connected = await checkConnection();
        if (!connected) return;
    }

    showToast('🚀 Iniciando Demo Rápida...', 'info');

    const btn = $('#btnDemo');
    btn.disabled = true;

    try {
        // Step 1: Create token
        showToast('Paso 1/4: Creando Token ACCESA...', 'info');
        await createToken();
        await sleep(1000);

        // Step 2: Create users
        showToast('Paso 2/4: Creando agentes de usuario...', 'info');

        const users = [
            { user_id: 'maria_lopez', accessibility_needs: ['visual_impairment'], initial_budget: 500 },
            { user_id: 'carlos_ruiz', accessibility_needs: ['hearing_impairment'], initial_budget: 300 },
            { user_id: 'ana_martinez', accessibility_needs: ['mobility'], initial_budget: 200 },
        ];

        for (const user of users) {
            const result = await apiCall('/agent/user/create', 'POST', user);
            state.userAgents.push(result);
            renderUserAgent(result);
            await sleep(500);
        }
        updateTxUserSelect();
        await sleep(500);

        // Step 3: Create services
        showToast('Paso 3/4: Creando agentes de servicio...', 'info');

        const services = ['Municipalidad_Mendoza', 'Hospital_Central'];
        for (const name of services) {
            const result = await apiCall('/agent/service/create', 'POST', { building_name: name });
            state.serviceAgents.push(result);
            renderServiceAgent(result);
            await sleep(500);
        }

        await refreshStats();
        await sleep(500);

        // Step 4: Execute transactions
        showToast('Paso 4/4: Ejecutando transacciones agente-a-agente...', 'info');

        const txs = [
            { user_id: 'maria_lopez', service_type: 'visual_impairment' },
            { user_id: 'carlos_ruiz', service_type: 'hearing_impairment' },
            { user_id: 'ana_martinez', service_type: 'mobility' },
        ];

        const serviceLabels = {
            visual_impairment: 'Guía de Voz',
            hearing_impairment: 'Videos Lengua de Señas',
            mobility: 'Mapa Accesible',
        };

        const animEl = $('#txAnimation');
        animEl.classList.remove('hidden');

        for (const tx of txs) {
            state.txCount++;
            $('#txAnimUser').textContent = tx.user_id;
            $('#txAnimService').textContent = serviceLabels[tx.service_type];

            try {
                const result = await apiCall('/agent/transaction', 'POST', tx);
                const cost = result.service?.price || '?';
                $('#txAnimAmount').textContent = `${cost} ACCESA`;

                addTransactionRow({
                    num: state.txCount,
                    user: tx.user_id,
                    service: serviceLabels[tx.service_type],
                    cost: `${cost} ACCESA`,
                    status: result.status,
                });
            } catch (err) {
                addTransactionRow({
                    num: state.txCount,
                    user: tx.user_id,
                    service: serviceLabels[tx.service_type],
                    cost: '—',
                    status: 'rejected',
                });
            }

            await sleep(1500);
        }

        await refreshStats();
        showToast('🏆 ¡Demo completada exitosamente!', 'success');
    } catch (error) {
        showToast(`Error en demo: ${error.message}`, 'error');
    } finally {
        btn.disabled = false;
    }
}

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

// ===== NAVIGATION =====
function setupNavigation() {
    $$('.nav__link').forEach((link) => {
        link.addEventListener('click', (e) => {
            $$('.nav__link').forEach((l) => l.classList.remove('active'));
            link.classList.add('active');
        });
    });
}

// ===== INITIALIZE =====
function init() {
    // Event listeners
    $('#btnConnect').addEventListener('click', checkConnection);
    $('#btnDemo').addEventListener('click', runDemo);
    $('#btnCreateToken').addEventListener('click', createToken);
    $('#formUserAgent').addEventListener('submit', createUserAgent);
    $('#formServiceAgent').addEventListener('submit', createServiceAgent);
    $('#formTransaction').addEventListener('submit', executeTransaction);

    setupNavigation();

    // Try auto-connect
    setTimeout(() => checkConnection(), 500);

    console.log('🏙️ ACCESA Smart Cities Dashboard initialized');
}

document.addEventListener('DOMContentLoaded', init);
