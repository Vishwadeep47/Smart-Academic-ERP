// Handle sidebar toggle on mobile devices
document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const body = document.querySelector('body');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            body.classList.toggle('sidebar-open');
        });
    }
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(event) {
        if (body.classList.contains('sidebar-open') && 
            !event.target.closest('.dashboard-sidebar') && 
            !event.target.closest('.sidebar-toggle')) {
            body.classList.remove('sidebar-open');
        }
    });
    
    // Set active nav item based on current page
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
    
    // Toggle between login and register forms
    const loginTab = document.getElementById('login-tab');
    const registerTab = document.getElementById('register-tab');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    
    if (loginTab && registerTab) {
        loginTab.addEventListener('click', function() {
            loginTab.classList.add('active');
            registerTab.classList.remove('active');
            loginForm.classList.add('active', 'show');
            registerForm.classList.remove('active', 'show');
        });
        
        registerTab.addEventListener('click', function() {
            registerTab.classList.add('active');
            loginTab.classList.remove('active');
            registerForm.classList.add('active', 'show');
            loginForm.classList.remove('active', 'show');
        });
    }
    
    // Handle flash messages auto-hide
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            message.style.transform = 'translateX(100%)';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
    
    // Form validation for login
    const loginFormEl = document.getElementById('login-form-element');
    if (loginFormEl) {
        loginFormEl.addEventListener('submit', function(event) {
            const enrollment = document.getElementById('login-enrollment').value;
            const password = document.getElementById('login-password').value;
            let isValid = true;
            
            if (!enrollment) {
                document.getElementById('login-enrollment-error').innerText = 'Enrollment number is required';
                isValid = false;
            } else {
                document.getElementById('login-enrollment-error').innerText = '';
            }
            
            if (!password) {
                document.getElementById('login-password-error').innerText = 'Password is required';
                isValid = false;
            } else {
                document.getElementById('login-password-error').innerText = '';
            }
            
            if (!isValid) {
                event.preventDefault();
            }
        });
    }
    
    // Form validation for registration
    const registerFormEl = document.getElementById('register-form-element');
    if (registerFormEl) {
        registerFormEl.addEventListener('submit', function(event) {
            const fullname = document.getElementById('register-fullname').value;
            const enrollment = document.getElementById('register-enrollment').value;
            const password = document.getElementById('register-password').value;
            const confirmPassword = document.getElementById('register-confirm-password').value;
            let isValid = true;
            
            if (!fullname) {
                document.getElementById('register-fullname-error').innerText = 'Full name is required';
                isValid = false;
            } else {
                document.getElementById('register-fullname-error').innerText = '';
            }
            
            if (!enrollment) {
                document.getElementById('register-enrollment-error').innerText = 'Enrollment number is required';
                isValid = false;
            } else {
                document.getElementById('register-enrollment-error').innerText = '';
            }
            
            if (!password) {
                document.getElementById('register-password-error').innerText = 'Password is required';
                isValid = false;
            } else if (password.length < 6) {
                document.getElementById('register-password-error').innerText = 'Password must be at least 6 characters';
                isValid = false;
            } else {
                document.getElementById('register-password-error').innerText = '';
            }
            
            if (password !== confirmPassword) {
                document.getElementById('register-confirm-password-error').innerText = 'Passwords do not match';
                isValid = false;
            } else {
                document.getElementById('register-confirm-password-error').innerText = '';
            }
            
            if (!isValid) {
                event.preventDefault();
            }
        });
    }
});
