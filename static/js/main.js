
function getSymbol(){
    var text = document.getElementById('myInput').value;
    console.log(text);
    return window.location.pathname = '/SYMBOL/'+text.toUpperCase();

}


function getAnalysis(){
	var symbol =document.getElementById('sym');
    var indicator_name = document.getElementById('myInput1');
    var period = document.getElementById('myInput2');
    var unit = document.getElementById('myInput3');
    return window.location.pathname = '/SYMBOL/'+symbol.innerText+'/Analysis/'+indicator_name.value+'/'+period.value+'/'+unit.value;

}