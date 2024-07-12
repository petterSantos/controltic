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
document.addEventListener('DOMContentLoaded', (event) => {
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
const buscarEquipo = async () =>{
    try{
        const esPatrimonizado = qs('#' + 'incEsEquipoPatrimonizado');
        if (esPatrimonizado.checked) {
                codPatrimonial =  $("#inc_codPatrimonial").val();
                // buscar en base interna
                //buscar en base externa
                const response = await fetch("http://127.0.0.1:4200/task/search_equipo/"+codPatrimonial+'/');
                const data = await response.json();
                console.log(data);
        
                let content = `<p class="text-start text-break fs-6 fw-normal" 
                                id="inc_textEstado">
                                Buscando en BD Externa
                              </p>`; 
                inc_textEstado.innerHTML = content; 

                let tipo = data.tipo[0]['tipoEquipoExt']
                data.equipos.forEach((equipo,index) => {
                        inc_equipoCodPatrimonial.value = equipo.codInterno;
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
                
        } else {
           // setDisplayNone(divId);
        }

    }catch (ex){
        alert(ex);
    }
}