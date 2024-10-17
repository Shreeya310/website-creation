function calculator(e){
    form.screen.value+=e.value;
}
function Clear(){
    form.screen.value=null;
}
function ev(){
    form.screen.value=eval(form.screen.value)
}