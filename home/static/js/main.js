let hide = document.querySelector('.s-hide');
let input = document.querySelector('.boxin');


hide.onclick = ()=>{
    hide.classList.add('show')
    if(input.type ==='password'){
        input.type = 'text';
    }else{
        input.type = 'password';
    }
};
