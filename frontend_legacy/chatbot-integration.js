(function() {
    const API_URL = 'https://cblue-ai.onrender.com';
    
    const chatbotHTML = `
        <style>
            #cblue-chat-header { background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;padding:10px 16px;display:flex;justify-content:space-between;align-items:center;border-radius:16px 16px 0 0;min-height:50px; }
            #cblue-chat-header-content { display:flex;align-items:center;gap:8px;flex:1;min-width:0; }
            #cblue-chat-header-text { display:flex;flex-direction:column;min-width:0; }
            #cblue-chat-header-text h3 { margin:0;font-size:14px;white-space:nowrap; }
            #cblue-chat-header-text small { opacity:0.9;font-size:11px; }
            @media (max-width: 768px) {
                #cblue-chat-window { width: calc(100vw - 20px) !important; max-width: 380px !important; height: calc(100vh - 120px) !important; max-height: 600px !important; right: 10px !important; bottom: 80px !important; left: 10px !important; margin: 0 auto !important; }
                #cblue-chat-button { width: 56px !important; height: 56px !important; bottom: 12px !important; right: 12px !important; }
                #cblue-chat-header { padding: 8px 12px !important; min-height: 42px !important; }
                #cblue-chat-header-content { gap: 6px !important; }
                #cblue-chat-header-content div:first-child { width: 28px !important; height: 28px !important; }
                #cblue-chat-header-text h3 { font-size: 12px !important; }
                #cblue-chat-header-text small { font-size: 10px !important; }
                #cblue-chat-close { font-size: 22px !important; }
                #cblue-chat-messages { padding: 14px !important; }
                #cblue-chat-input { font-size: 16px !important; padding: 11px 14px !important; }
                .chat-message-user { max-width: 75% !important; }
                .chat-message-bot { max-width: 80% !important; }
            }
            @media (max-width: 480px) {
                #cblue-chat-window { width: calc(100vw - 16px) !important; right: 8px !important; left: 8px !important; bottom: 76px !important; }
                #cblue-chat-header { padding: 7px 10px !important; min-height: 40px !important; }
                #cblue-chat-header-content { gap: 5px !important; }
                #cblue-chat-header-content div:first-child { width: 26px !important; height: 26px !important; }
                #cblue-chat-header-text h3 { font-size: 11px !important; }
                #cblue-chat-header-text small { font-size: 9px !important; }
                #cblue-chat-close { font-size: 20px !important; }
                #cblue-chat-messages { padding: 12px !important; }
            }
            @media (max-width: 430px) {
                #cblue-chat-window { height: calc((100vh - 120px) * 0.7) !important; max-height: 420px !important; }
            }
            @media (max-width: 375px) {
                #cblue-chat-window { width: calc(100vw - 12px) !important; max-width: 363px !important; height: calc(100vh - 140px) !important; max-height: 480px !important; right: 6px !important; left: 6px !important; bottom: 70px !important; }
                #cblue-chat-button { width: 50px !important; height: 50px !important; bottom: 10px !important; right: 10px !important; }
                #cblue-chat-header { padding: 6px 8px !important; min-height: 38px !important; }
                #cblue-chat-header-content div:first-child { width: 24px !important; height: 24px !important; }
                #cblue-chat-header-text h3 { font-size: 11px !important; }
                #cblue-chat-header-text small { font-size: 8px !important; }
                #cblue-chat-close { font-size: 18px !important; }
                #cblue-chat-messages { padding: 10px !important; }
                #cblue-chat-input { padding: 9px 12px !important; font-size: 16px !important; }
                .chat-message-user, .chat-message-bot { max-width: 70% !important; font-size: 13px !important; padding: 8px 12px !important; }
            }
        </style>
        <div id="cblue-chatbot-container" style="position:fixed;bottom:20px;right:20px;z-index:10000">
            <button id="cblue-chat-button" style="width:60px;height:60px;border-radius:30px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border:none;box-shadow:0 4px 12px rgba(0,0,0,0.15);cursor:pointer;transition:transform 0.3s" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                <svg viewBox="0 0 24 24" style="width:28px;height:28px;fill:white"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
            </button>
            <div id="cblue-chat-window" style="display:none;position:fixed;bottom:90px;right:20px;width:280px;height:480px;background:white;border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,0.15);flex-direction:column">
                <div id="cblue-chat-header">
                    <div id="cblue-chat-header-content">
                        <div style="width:30px;height:30px;background:white;border-radius:50%;display:flex;align-items:center;justify-content:center;overflow:hidden;flex-shrink:0"><img src="Customer Support Emoji.png" style="width:100%;height:100%;object-fit:cover" alt="AI"></div>
                        <div id="cblue-chat-header-text"><h3>Cblue AI Assistant</h3><small>ออนไลน์</small></div>
                    </div>
                    <button id="cblue-chat-close" style="background:none;border:none;color:white;cursor:pointer;font-size:24px;line-height:1;flex-shrink:0">×</button>
                </div>
                <div id="cblue-chat-messages" style="flex:1;overflow-y:auto;padding:20px;background:#f7f8fa"></div>
                <div style="padding:16px;background:white;border-radius:0 0 16px 16px">
                    <form id="cblue-chat-input-form" style="display:flex;gap:8px">
                        <input type="text" id="cblue-chat-input" placeholder="พิมพ์ข้อความของคุณ..." style="flex:1;padding:12px 16px;border:1px solid #e0e0e0;border-radius:24px;outline:none;font-size:14px"/>
                        <button type="submit" style="width:44px;height:44px;border-radius:50%;background:#667eea;border:none;cursor:pointer;transition:background 0.3s" onmouseover="this.style.background='#5568d3'" onmouseout="this.style.background='#667eea'">
                            <svg viewBox="0 0 24 24" style="width:20px;height:20px;fill:white"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    `;
    
    document.addEventListener('DOMContentLoaded', function() {
        document.body.insertAdjacentHTML('beforeend', chatbotHTML);
        
        const btn = document.getElementById('cblue-chat-button');
        const win = document.getElementById('cblue-chat-window');
        const close = document.getElementById('cblue-chat-close');
        const form = document.getElementById('cblue-chat-input-form');
        const input = document.getElementById('cblue-chat-input');
        const msgs = document.getElementById('cblue-chat-messages');
        
        btn.onclick = () => { win.style.display = 'flex'; setTimeout(() => input.focus(), 100); };
        close.onclick = () => { win.style.display = 'none'; input.blur(); };
        
        form.onsubmit = async (e) => {
            e.preventDefault();
            const msg = input.value.trim();
            if (!msg) return;
            input.value = '';
            
            msgs.innerHTML += '<div style="margin-bottom:16px;display:flex;flex-direction:row-reverse;gap:8px"><div style="width:32px;height:32px;border-radius:50%;background:#667eea;color:white;display:flex;align-items:center;justify-content:center;flex-shrink:0">👤</div><div class="chat-message-user" style="padding:10px 14px;border-radius:16px;background:#667eea;color:white;max-width:220px;word-wrap:break-word;font-size:14px">' + msg + '</div></div>';
            msgs.scrollTop = msgs.scrollHeight;
            
            const loadingId = 'loading-' + Date.now();
            msgs.innerHTML += '<div id="' + loadingId + '" style="margin-bottom:16px;display:flex;gap:8px"><div style="width:32px;height:32px;border-radius:50%;background:#e8eaf6;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden"><img src="Customer Support Emoji.png" style="width:100%;height:100%;object-fit:cover" alt="AI"></div><div class="chat-message-bot" style="padding:10px 14px;border-radius:16px;background:white;border:1px solid #e0e0e0;max-width:220px;font-size:13px">กำลังคิด...</div></div>';
            msgs.scrollTop = msgs.scrollHeight;
            
            try {
                const r = await fetch(API_URL + '/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: msg })
                });
                const d = await r.json();
                document.getElementById(loadingId).remove();
                const responseText = d.message || 'ขออภัย ไม่ได้รับการตอบกลับ กรุณาติดต่อ: cblue.thailand@gmail.com';
                const formattedResponse = responseText.replace(/•\s*/g, '<br>• ');
                msgs.innerHTML += '<div style="margin-bottom:16px;display:flex;gap:8px"><div style="width:32px;height:32px;border-radius:50%;background:#e8eaf6;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden"><img src="Customer Support Emoji.png" style="width:100%;height:100%;object-fit:cover" alt="AI"></div><div class="chat-message-bot" style="padding:10px 14px;border-radius:16px;background:white;border:1px solid #e0e0e0;max-width:220px;word-wrap:break-word;font-size:13px;white-space:pre-line">' + formattedResponse + '</div></div>';
                msgs.scrollTop = msgs.scrollHeight;
            } catch (err) {
                console.error(err);
                document.getElementById(loadingId).remove();
                msgs.innerHTML += '<div style="margin-bottom:16px;display:flex;gap:8px"><div style="width:32px;height:32px;border-radius:50%;background:#e8eaf6;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden"><img src="Customer Support Emoji.png" style="width:100%;height:100%;object-fit:cover" alt="AI"></div><div class="chat-message-bot" style="padding:10px 14px;border-radius:16px;background:white;border:1px solid #e0e0e0;max-width:220px;font-size:13px">เกิดข้อผิดพลาด กรุณาติดต่อ: cblue.thailand@gmail.com</div></div>';
                msgs.scrollTop = msgs.scrollHeight;
            }
        };
    });
})();
