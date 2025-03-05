function validateForm() {
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;
    
    if (!email.includes("@") || !phone.match(/^\d{10}$/)) {
        alert("Invalid email or phone number");
        return false;
    }
    return true;
}
