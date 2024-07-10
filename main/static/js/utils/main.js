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
});

////////////////////////////////////////////////////////////////

// const checkboxesTotal = qsa('input[type="checkbox"]').length;
showContent();

////////////////////////////////////////////////////////////////
// CARGAR EQUIPO EN CONSULTA
const buscarEquipo = async () =>{
    try{
        codPatrimonial =  $("#inc_codPatrimonial").val();
        const response = await fetch("http://127.0.0.1:4200/task/search_equipo/"+codPatrimonial+'/');
        const data = await response.json();
        console.log(data);

        let content = ``; 
        let tipo = data.tipo[0]['tipoEquipoExt']
      data.equipos.forEach((equipo,index) => {
            content += `
                           <div>Cod Patrimonial: ${equipo.codInterno}</div>
                           <div>Tipo Equipo: ${tipo}</div>
                           <div>Marca: ${equipo.marca}</div>
                           <div>Modelo: ${equipo.modelo}</div>
                           <div>Nro Serie: ${equipo.nroSerie}</div>
                           <div>Color: ${equipo.color}</div>
                           <div>FechaPecosa: ${equipo.fechaPecosa}</div>
                           <div>Estado: ${equipo.estado}</div>
                           <div>Observacion: ${equipo.descOtros}</div>
                           <div>Tipo Doc: ${equipo.tipoDocAdq}</div>
                           <div>Nro Doc: ${equipo.docAdq}</div>
                           <div>Nro SIAF:${equipo.siaf}</div>
            `
      });
        inc_equipoEncontrado.innerHTML = content;
    }catch (ex){
        alert(ex);
    }
}