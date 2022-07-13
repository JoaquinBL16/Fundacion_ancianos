$(document).ready(function () {
    
    $("#register-form").submit(function (event) { 
        // event.preventDefault();

        let userName = $("#userName").val();
        let userApellido = $("#userApellido").val();
        let userEmail = $("#userEmail").val();
        let userPassword = $("#userPassword").val();

        

        // if (userEmail === "usuario@gmail.com" && userPassword === "usuario") {
        //     alert("Bienvenido, ingresando a tu perfil...");
        //     window.location.replace("../../usuario/inicio/");
        //     return
        // } 

        if (userEmail === "donador@gmail.com" && userPassword === "donador") {
            alert("Bienvenido donador, ingresando a tu perfil...");
            window.location.replace("../../donador/inicio/");
            return
        } 

        // alert("Clave o usuario incorrecto, intenta denuevo");

    });
    

});