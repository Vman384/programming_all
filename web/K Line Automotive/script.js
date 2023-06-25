var navLinks = document.getElementById("navLinks");

function showMenu(){
    navLinks.style.right= "0";
}
function hideMenu(){
    navLinks.style.right= "-200px";
}

function SendEmail(){
    Email.send({
        SecureToken : "Your-Secure-Token",
        To : 'email',
        From : "your-email@gmail.com",
        Subject : "New Enquiry",
        Body : "Name: " + document.getElementById("name").value
        + "<br> Email: " + document.getElementById("email").value
        + "<br> Phone number: " + document.getElementById("phone").value
        + "<br> Message: " + document.getElementById("message").value
    }).then(
        message => alert("Message Sent Successfully")
    );
    }