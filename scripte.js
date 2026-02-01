document.addEventListener('DOMContentLoaded', () => {
    const typewriter = document.getElementById('typewriter');
    const dashboard = document.getElementById('main-content');
    const loader = document.getElementById('loader-wrapper');
    
    const messages = ["BOOTING CORE...", "SYNCING DATABASE...", "SYSTEM READY."];
    let mIdx = 0, charIdx = 0;

    function type() {
        if (!typewriter) return;
        if (mIdx < messages.length) {
            if (charIdx < messages[mIdx].length) {
                typewriter.textContent += messages[mIdx][charIdx];
                charIdx++;
                setTimeout(type, 50);
            } else {
                setTimeout(() => {
                    typewriter.textContent = "";
                    charIdx = 0; mIdx++;
                    type();
                }, 600);
            }
        }
    }

    type();

    // FORCE reveal dashboard after 3 seconds
    setTimeout(() => {
        if (loader) {
            loader.style.opacity = '0';
            setTimeout(() => loader.classList.add('hidden'), 500);
        }
        if (dashboard) {
            dashboard.classList.add('fade-in');
        }
    }, 3000);
});