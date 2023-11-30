



function like(slug,pk){
    var element = document.getElementById('like')
    var count = document.getElementById('count')
    $.get(`/course/like/${slug}/${pk}`).then(response =>{
        if(response['response'] === 'liked'){
            element.className = 'bi bi-heart-fill'
            count.innerText = Number(count.innerText) + 1
        }else{
            element.className = 'bi bi-heart'
             count.innerText = Number(count.innerText) - 1
        }
    })
}