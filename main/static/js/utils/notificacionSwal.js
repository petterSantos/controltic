const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon, // warning, success, error, info
        confirmButtonText: confirmButtonText
    })
}

const preguntarEliminacion =(nameTable,url) =>{
    Swal.fire({
        title: "¿Confirma la eliminacion de la "+nameTable+"?",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminarlo!",
        backdrop: true,
        showLoaderOnConfirm: true,
        preConfirm: () => {
            location.href = url;
        },
        allowOutsideClick: () => false,
        allowEscapeKey: () => false
     })
}
