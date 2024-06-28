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

function showContent() // OCULTAR O MOSTRAR DIV CON UN CHECKBOX
{
        const checkboxId = 'incSolicTieneDoc';
        const divId = 'div_incSolicDoc';

        const checkboxNode = qs('#' + checkboxId);
        checkboxNode.addEventListener('click', function () // void
        {
            if (checkboxNode.checked) {
                setDisplayBlock(divId);
            } else {
                setDisplayNone(divId);
            }
        });

}

///para cargar equipos y dataTable
let dataTable;
let dataTableIsInitialized = false;

const initDatataTable = async () =>{
    if(dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listEquipos();

    dataTable = $('#tableBody_listarEquipos').DataTable({});

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
});

////////////////////////////////////////////////////////////////

// const checkboxesTotal = qsa('input[type="checkbox"]').length;
showContent();