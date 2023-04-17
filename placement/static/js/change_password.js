const currentPasswordInput = document.getElementById('current-password');
const currentPasswordErrorSpan = document.getElementById('current-password-error');
const newPasswordInput = document.getElementById('new-password');
const newPasswordErrorSpan = document.getElementById('new-password-error');
const confirmPasswordInput = document.getElementById('confirm-password');
const confirmPasswordErrorSpan = document.getElementById('confirm-password-error');

currentPasswordInput.addEventListener('input', validateCurrentPassword);
newPasswordInput.addEventListener('input', validateNewPassword);
confirmPasswordInput.addEventListener('input', validateConfirmPassword);
function validateCurrentPassword() {
    const currentPassword = currentPasswordInput.value;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{6,}$/;
    if (passwordRegex.test(currentPassword)) {
        currentPasswordErrorSpan.textContent = '';
        return true;
    } else {
        currentPasswordErrorSpan.textContent = '* Password pattern not matches';
        currentPasswordErrorSpan.style.color = 'red';
        return false;
    }
}

function validateNewPassword() {
    const newPassword = newPasswordInput.value;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{6,}$/;
    if (passwordRegex.test(newPassword)) {
        newPasswordErrorSpan.textContent = '';
        return true;
    } else {
        newPasswordErrorSpan.innerHTML = '* New password must be at least 6 characters, at least one capital letter, one special character, and one number';
        newPasswordErrorSpan.style.color = 'red';
        return false;
    }
}

function validateConfirmPassword() {
    const confirmPassword = confirmPasswordInput.value;
    if (confirmPassword !== newPasswordInput.value) {
        confirmPasswordErrorSpan.textContent = '* Passwords do not match';
        confirmPasswordErrorSpan.style.color = 'red';
        return false;
    } else {
        confirmPasswordErrorSpan.textContent = '';
        return true;
    }
}
