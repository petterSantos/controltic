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

function showContent() // void
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

////////////////////////////////////////////////////////////////

// const checkboxesTotal = qsa('input[type="checkbox"]').length;
showContent();