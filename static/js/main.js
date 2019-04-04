
function getSymbol(){
    var text = document.getElementById('myInput').value;
    console.log(text);
    return window.location.pathname = '/SYMBOL/'+text.toUpperCase();

}