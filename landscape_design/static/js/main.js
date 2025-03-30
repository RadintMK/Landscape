function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    } else {
        console.error('Modal with ID ' + modalId + ' not found!');
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        const anyActiveModal = document.querySelector('.modal-overlay.active');
        if (!anyActiveModal) {
             document.body.style.overflow = 'auto';
        }
    } else {
        console.error('Modal with ID ' + modalId + ' for closing not found!');
    }
}


if (typeof openLoginModal === 'undefined') {
    function openLoginModal() {
        openModal('loginModal');
    }
}

if (typeof openRegisterModal === 'undefined') {
    function openRegisterModal() {
        openModal('registerModal');
    }
}

if (typeof openBlogModal === 'undefined') {
    function openBlogModal(postId) {
        openModal('blog-' + postId);
    }
}

if (typeof openPortfolioModal === 'undefined') {
    function openPortfolioModal(projectId) {
        openModal('portfolio-' + projectId);
    }
}


document.addEventListener('DOMContentLoaded', () => {

    const closeButtons = document.querySelectorAll('.modal-close');
    closeButtons.forEach(button => {
        const modalOverlay = button.closest('.modal-overlay');
        if (modalOverlay) {
            const modalId = modalOverlay.getAttribute('id');
            if (modalId) {
                button.addEventListener('click', () => closeModal(modalId));
            }
        }
    });

    const modalOverlays = document.querySelectorAll('.modal-overlay');
    modalOverlays.forEach(overlay => {
        overlay.addEventListener('click', (event) => {
            if (event.target === overlay) {
                 const modalId = overlay.getAttribute('id');
                 if (modalId) {
                    closeModal(modalId);
                 }
            }
        });
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === "Escape") {
            const activeModal = document.querySelector('.modal-overlay.active');
            if (activeModal) {
                 const modalId = activeModal.getAttribute('id');
                 if (modalId) {
                    closeModal(modalId);
                 }
            }
        }
    });

    const portfolioFilterButtons = document.querySelectorAll('.portfolio-filters .portfolio-filter');
    const portfolioItems = document.querySelectorAll('.portfolio-gallery .portfolio-item');

    if (portfolioFilterButtons.length > 0 && portfolioItems.length > 0) {
        portfolioFilterButtons.forEach(button => {
            button.addEventListener('click', () => {
                portfolioFilterButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                const filterValue = button.getAttribute('data-filter');

                portfolioItems.forEach(item => {
                    const itemCategory = item.getAttribute('data-category');
                    if (filterValue === 'all' || itemCategory === filterValue) {
                       item.hidden = false;
                    } else {
                        item.hidden = true;
                    }
                });
            });
        });
    }

    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('AJAX для входа пока не реализован');
        });
    }

    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('AJAX для регистрации пока не реализован');
        });
    }

});