function bloglike(slug,id){

    var element = document.getElementById('bloglike')
    var count1 = document.getElementById('count1')
    $.get(`/blog/test/${slug}/${id}`).then(response =>{
       if(response['response'] === 'liked'){
           element.className = 'bi bi-heart-fill'
           count1.innerText = Number(count1.innerText) + 1
       }else {
           element.className = 'bi bi-heart'
           count1.innerText = Number(count1.innerText) - 1
       }
    })
}



