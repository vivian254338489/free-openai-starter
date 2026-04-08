/**
 * Free OpenAI-Starter Web Demo
 * Handles API configuration and chat interactions
 */

// Storage keys
const STORAGE_KEYS = {
    API_KEY: 'openai_starter_api_key',
    BASE_URL: 'openai_starter_base_url',
    MODEL: 'openai_starter_model',
    MESSAGES: 'openai_starter_messages'
};

// Defaults
const DEFAULTS = {
    BASE_URL: 'https://www.tken.shop/v1',
    MODEL: 'gpt-4o-mini'
};

// DOM Elements
let elements = {};
let isLoading = false;

/**
 * Initialize the app
 */
function init() {
    cacheElements();
    loadSettings();
    loadMessages();
    setupEventListeners();
}

/**
 * Cache DOM elements
 */
function cacheElements() {
    elements = {
        apiKey: document.getElementById('api-key'),
        baseUrl: document.getElementById('base-url'),
        model: document.getElementById('model'),
        saveSettings: document.getElementById('save-settings'),
        resetSettings: document.getElementById('reset-settings'),
        chatOutput: document.getElementById('chat-output'),
        promptInput: document.getElementById('prompt-input'),
        sendBtn: document.getElementById('send-btn'),
        clearChat: document.getElementById('clear-chat'),
        errorDisplay: document.getElementById('error-display')
    };
}

/**
 * Setup event listeners
 */
function setupEventListeners() {
    elements.saveSettings.addEventListener('click', saveSettings);
    elements.resetSettings.addEventListener('click', resetSettings);
    elements.sendBtn.addEventListener('click', sendMessage);
    elements.clearChat.addEventListener('click', clearChat);
    elements.promptInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
}

/**
 * Load settings from localStorage
 */
function loadSettings() {
    elements.apiKey.value = localStorage.getItem(STORAGE_KEYS.API_KEY) || '';
    elements.baseUrl.value = localStorage.getItem(STORAGE_KEYS.BASE_URL) || DEFAULTS.BASE_URL;
    elements.model.value = localStorage.getItem(STORAGE_KEYS.MODEL) || DEFAULTS.MODEL;
}

/**
 * Save settings to localStorage
 */
function saveSettings() {
    const apiKey = elements.apiKey.value.trim();
    const baseUrl = elements.baseUrl.value.trim();
    const model = elements.model.value.trim();

    if (!apiKey) {
        showError('Please enter your API key');
        return;
    }

    if (!baseUrl || !baseUrl.endsWith('/v1')) {
        showError('Base URL must end with /v1');
        return;
    }

    localStorage.setItem(STORAGE_KEYS.API_KEY, apiKey);
    localStorage.setItem(STORAGE_KEYS.BASE_URL, baseUrl);
    localStorage.setItem(STORAGE_KEYS.MODEL, model || DEFAULTS.MODEL);

    hideError();
    alert('Settings saved!');
}

/**
 * Reset settings to defaults
 */
function resetSettings() {
    elements.apiKey.value = '';
    elements.baseUrl.value = DEFAULTS.BASE_URL;
    elements.model.value = DEFAULTS.MODEL;
    localStorage.removeItem(STORAGE_KEYS.API_KEY);
    localStorage.removeItem(STORAGE_KEYS.BASE_URL);
    localStorage.removeItem(STORAGE_KEYS.MODEL);
}

/**
 * Load messages from localStorage
 */
function loadMessages() {
    const saved = localStorage.getItem(STORAGE_KEYS.MESSAGES);
    if (saved) {
        try {
            const messages = JSON.parse(saved);
            messages.forEach(msg => addMessageToUI(msg.role, msg.content));
        } catch (e) {
            console.error('Failed to load messages:', e);
        }
    }
}

/**
 * Save messages to localStorage
 */
function saveMessages() {
    const messages = [];
    document.querySelectorAll('.message:not(.welcome-message)').forEach(el => {
        if (el.classList.contains('user') || el.classList.contains('assistant')) {
            const role = el.classList.contains('user') ? 'user' : 'assistant';
            const content = el.querySelector('.message-content').textContent;
            messages.push({ role, content });
        }
    });
    localStorage.setItem(STORAGE_KEYS.MESSAGES, JSON.stringify(messages));
}

/**
 * Add message to chat UI
 */
function addMessageToUI(role, content) {
    // Remove welcome message if exists
    const welcome = elements.chatOutput.querySelector('.welcome-message');
    if (welcome) welcome.remove();

    const message = document.createElement('div');
    message.className = `message ${role}`;
    message.innerHTML = `<div class="message-content">${escapeHtml(content)}</div>`;
    elements.chatOutput.appendChild(message);
    scrollToBottom();
}

/**
 * Send message to API
 */
async function sendMessage() {
    if (isLoading) return;

    const prompt = elements.promptInput.value.trim();
    if (!prompt) return;

    const apiKey = localStorage.getItem(STORAGE_KEYS.API_KEY);
    const baseUrl = localStorage.getItem(STORAGE_KEYS.BASE_URL) || DEFAULTS.BASE_URL;
    const model = localStorage.getItem(STORAGE_KEYS.MODEL) || DEFAULTS.MODEL;

    if (!apiKey) {
        showError('Please configure your API key first');
        return;
    }

    // Add user message
    addMessageToUI('user', prompt);
    elements.promptInput.value = '';
    saveMessages();

    // Show loading
    isLoading = true;
    updateSendButton();
    showLoading();

    try {
        const response = await fetch(`${baseUrl}/chat/completions`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: model,
                messages: [{ role: 'user', content: prompt }]
            })
        });

        hideLoading();

        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(error.error?.message || `HTTP ${response.status}`);
        }

        const data = await response.json();
        const assistantContent = data.choices?.[0]?.message?.content || 'No response';

        addMessageToUI('assistant', assistantContent);
        saveMessages();

    } catch (error) {
        hideLoading();
        addMessageToUI('error', `Error: ${error.message}`);
        saveMessages();
    }

    isLoading = false;
    updateSendButton();
}

/**
 * Show loading indicator
 */
function showLoading() {
    const loading = document.createElement('div');
    loading.className = 'message assistant loading';
    loading.id = 'loading-indicator';
    loading.innerHTML = `
        <div class="message-content">
            <div class="loading">
                <div class="loading-dots"><span></span><span></span><span></span></div>
                <span>Thinking...</span>
            </div>
        </div>
    `;
    elements.chatOutput.appendChild(loading);
    scrollToBottom();
}

/**
 * Hide loading indicator
 */
function hideLoading() {
    const loading = document.getElementById('loading-indicator');
    if (loading) loading.remove();
}

/**
 * Clear chat
 */
function clearChat() {
    elements.chatOutput.innerHTML = `
        <div class="welcome-message">
            <p>Configure your API settings above, then send a test prompt.</p>
        </div>
    `;
    localStorage.removeItem(STORAGE_KEYS.MESSAGES);
}

/**
 * Update send button state
 */
function updateSendButton() {
    const hasPrompt = elements.promptInput.value.trim().length > 0;
    const hasApiKey = localStorage.getItem(STORAGE_KEYS.API_KEY);
    elements.sendBtn.disabled = !hasPrompt || !hasApiKey || isLoading;
}

/**
 * Show error message
 */
function showError(message) {
    elements.errorDisplay.textContent = message;
    elements.errorDisplay.classList.remove('hidden');
}

/**
 * Hide error message
 */
function hideError() {
    elements.errorDisplay.classList.add('hidden');
}

/**
 * Scroll chat to bottom
 */
function scrollToBottom() {
    elements.chatOutput.scrollTop = elements.chatOutput.scrollHeight;
}

/**
 * Escape HTML
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Start
document.addEventListener('DOMContentLoaded', init);
