
document.addEventListener('DOMContentLoaded',function(){
    var plusBtn = document.querySelector('.btn-plus');
    var minusBtn = document.querySelector('.btn-minus');
    var inputField = document.querySelector('.form-control');

    plusBtn.addEventListener('click',function(){
        var value = parseInt(inputField.value);
        if(value<100){
            inputField.value = value + 1;
        }
    });
    minusBtn.addEventListener('click',function(){
        var value = parseInt(inputField.value);
        if(value>1){
            inputField.value = value - 1;
        }
    });
});
