$(function () {
    $("#incSolicitante").select2();
    $("#incSolicOficina").select2();
  
});

function qs(selector) // js node
{
    return document.querySelector(selector);
}
function qsa(selector) // js node
{
    return document.querySelectorAll(selector);
}
function setDisplayBlock(elementId) // void
{
    qs('#' + elementId).style.display = 'block';
}
function setDisplayNone(elementId) // void
{
    qs('#' + elementId).style.display = 'none';
}

// OCULTAR O MOSTRAR DIV CON UN CHECKBOX
function showDiv_checkbox(idCheckBox,idDiv){
        const checkboxId = idCheckBox;
        const divId = idDiv;

        const checkboxNode = qs('#' + checkboxId);
        if (checkboxNode.checked) {
            setDisplayBlock(divId);
        } else {
            setDisplayNone(divId);
        }

        checkboxNode.addEventListener('click', function () // void
        {
            if (checkboxNode.checked) {
                setDisplayBlock(divId);
            } else {
                setDisplayNone(divId);
            }
        });
}
// cambiar el placeHolder de un input cuando cambiar de valor un checkBox
function changePlaceHolderInput_checkbox(idInput,idCheckBox){
    const inputId = idInput;
    const checkboxId = idCheckBox;

    const checkboxNode = qs('#' + checkboxId);
    qs('#' + inputId).value = "";

    if (checkboxNode.checked) {
         qs('#' + inputId).placeholder = 'cod. Patrimonial';
    } else {
        qs('#' + inputId).placeholder = 'nro. serie';
    }

    checkboxNode.addEventListener('click', function () // void
    {
        qs('#' + inputId).value = "";
        if (checkboxNode.checked) {
            qs('#' + inputId).placeholder = 'cod. Patrimonial';
        } else {
            qs('#' + inputId).placeholder = 'nro. serie';
        }
    });
}

////////////////////////////////////////////////////////////////

// const checkboxesTotal = qsa('input[type="checkbox"]').length;
//showContent();
var deleteImageUrl = null;
var checkImageUrl = null;
document.addEventListener('DOMContentLoaded', (event) => {
    //pasando imagen del servidor django --> javascript
    deleteImageUrl = document.getElementById('deleteImageUrl').textContent.trim();
    checkImageUrl = document.getElementById('checkImageUrl').textContent.trim();
    showDiv_checkbox('incSolicTieneDoc','div_incSolicDoc');
    changePlaceHolderInput_checkbox('inc_codPatrimonial','incEsEquipoPatrimonizado');
});

////////////////////////////////////////////////////////////////

///para cargar equipos y dataTable
let dataTable;
let dataTableIsInitialized = false;
const dataTableOptions =  {
    columnDefs : [
        { className: "centered",targets: [0,1,2,3,4]},
        { orderable: false,targets: [1,2]},
        { searchable: false,targets: [3]}
    ],
    pageLength: 4,
    destroy: true,
}
const initDatataTable = async () =>{
    if(dataTableIsInitialized) {
        dataTable.destroy();
    }
    await listEquipos();

    dataTable = $('#datatable-equipos').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listEquipos = async () => {
    try{
        const response = await fetch("http://127.0.0.1:4200/task/list_equipos/");
        const data = await response.json();

        let content = ``; 
        data.equipos.forEach((equipo,index) => {
            content += `
                <tr>
                    <td>${index+1}</td>
                    <td>${equipo.codPatrimonial}</td>
                    <td>${equipo.marca}</td>
                    <td>${equipo.modelo}</td>
                    <td>${equipo.modelo}</td>
                </tr>
            `
        });
        tableBody_listarEquipos.innerHTML = content;
    }catch (ex){
        alert(ex);
    }
};

window.addEventListener("load",async () => {
    await initDatataTable();
    document.getElementById('incSolicTieneDoc').addEventListener('change', function() {
        showContent('incSolicTieneDoc','div_incSolicDoc')
    });
});


// CARGAR EQUIPO EN CONSULTA
function colocarDatosEquipos(tipo,equipos,busqueda){
    equipos.forEach((equipo,index) => {
        if(busqueda == 'interno'){
            inc_equipoCodPatrimonial.value = equipo.codPatrimonial;
        }
        else {
           inc_equipoCodPatrimonial.value = equipo.codInterno; 
        };
        
        inc_equipoTipo.value = tipo;
        inc_equipoMarca.value = equipo.marca;
        inc_equipoModelo.value = equipo.modelo; 
        inc_equipoSerie.value = equipo.nroSerie;
        inc_equipoColor.value = equipo.color;
        inc_equipoFechaPecosa.value = equipo.fechaPecosa;
        inc_equipoEstado.value = equipo.estado;
        inc_equipoObservacion.value = equipo.descOtros;
        inc_equipoTipoDoc.value = equipo.tipoDocAdq;
        inc_equipoNroDoc.value = equipo.docAdq;
        inc_equipoSiaf.value = equipo.siaf;
    });
};

const buscarEquipo = async () =>{
    try{
        const esPatrimonizado = qs('#' + 'incEsEquipoPatrimonizado');
        codPatrimonial =  $("#inc_codPatrimonial").val();
        console.log('codpatrimonial: '+codPatrimonial);
        let content = ``;
        //es patrimonizado
        if (esPatrimonizado.checked) {
                try{
                    console.log('entrnado interno, kkegue hasta aca');
                    // buscar en base interna
                    const responseInterno = await fetch("http://127.0.0.1:4200/task/search_equipoInterno/"+codPatrimonial+'/');

                    if(!responseInterno.ok){
                  //      throw new Error('Error en la solicitud: ' + responseInterno.status);

                        //intentando en base externa
                        const response = await fetch("http://127.0.0.1:4200/task/search_equipo/"+codPatrimonial+'/');
    console.log('llegue hasta aca base externa');
                       //no se encontro en BD externa
                        if(!response.ok){
                            console.log('llegue hasta aca base externa, NO SE ESTABLECIO CONEXION');
                            content = `
                            <p class="text-start text-break fs-6 fw-normal">
                              <img src="${deleteImageUrl}" alt="rechazado" title="no se extablecio conexion con la BD" width="20" height="20">  Buscando en BD Externa
                             </p>
                            `
                        }
                        //si se econtro en BD externa
                        else {
                            console.log('llegue hasta aca, se encontro en base externa');
                            const data = await response.json();
                            
                            if (data.equipos.length > 0) {
                                colocarDatosEquipos(data.tipo,data.equipos,'externo');
                                content = `
                             <p class="text-start text-break fs-6 fw-normal">
                              <img src="${checkImageUrl}" alt="encontrado" title="encontrado" width="20" height="20">  Buscando en BD Externa
                             </p>
                             `; 
                            }
                            else {
                            content = `
                            <p class="text-start text-break fs-6 fw-normal">
                              <img src="${deleteImageUrl}" alt="rechazado" title="no encontrado" width="20" height="20">NO SE  ENCONTRO en BD Externa
                             </p>
                           `;  
                            }
                        }
                        
                    }
                    //se ecnontro en BD interna
                   else {
                    const dataInterno = await response.json();
                     if (dataInterno.equipos.length > 0) {
                        const dataInterno = await responseInterno.json();
                        let content = ``; 
                        colocarDatosEquipos(dataInterno.tipo,dataInterno.equipos,'interno');
                        console.log('ENCONTRO DATOS');
                        content = `
                        <p class="text-start text-break fs-6 fw-normal">
                          <img src="${checkImageUrl}" alt="encontrado" title="encontrado" width="20" height="20">  Buscando en BD Interna
                         </p>
                       `; 
                     }
                   }

                     div_inc_textEstado.innerHTML = content; 

                }catch (error){
                    console.error('Hubo un problema con la operación fetch:', error);
                }
                
        //SI NO ESTA PATRIMONIZADA
        } else {
            try{
                // buscar en base externa
                const response = await fetch("http://127.0.0.1:4200/task/search_equipo/"+codPatrimonial+'/');

                if(!response.ok){
                    throw new Error('Error en la solicitud: ' + response.status);
                }
                const data = await response.json();
                let content = ``; 

                if (data.equipos.length > 0) {
                    colocarDatosEquipos(data.tipo,data.equipos,'externo');
                    console.log('ENCONTRO DATOS EXTERNO');
                    content = `
                    <p class="text-start text-break fs-6 fw-normal">
                      <img src="${checkImageUrl}" alt="rechazado" title="no encontrado" width="20" height="20">  Buscando en BD Externa
                     </p>
                   `; 
                 }
                else {
                    console.log('NO SE ENCONTRO DATOS EXTERNO')
                    content = `
                    <p class="text-start text-break fs-6 fw-normal">
                      <img src="${deleteImageUrl}" alt="rechazado" title="no encontrado" width="20" height="20">  Buscando en BD Interna2
                     </p>
                   `; 
                 }

                 div_inc_textEstado.innerHTML = content; 

            }catch (error){
                console.error('Hubo un problema con la operación fetch:', error);
            }
        }

    }catch (ex){
        alert(ex);
    }
}