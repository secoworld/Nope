// // 是为点击为出现心形特效
// (function(w, d){
//     d.querySelector("body").addEventListener('click', function(e){
//         addLike(e);     // 添加特效
//     });

//     var likeArr = [];   // 用来存储队列，用于多个div
//     function addLike(e){
//         var like =  document.createElement("div");
//         like.classList.add("like");
//         like.innerHTML = '<i class="fas fa-heart"></i>';
//         d.body.appendChild(like);

//         // 将添加的输入进列表
//         likeArr.push({
//             el: like,
//             top : e.clientY - 10,
//             left: e.clientX - 20,
//             opacity: 1,
//             scale: 1,
//             color: `rgb(${Math.random()*255}, ${Math.random()*255}, ${Math.random()*255})`
//         });

//         moveLike();     //移动like
//     }

//     function moveLike(){
//         for(var i=0; i< likeArr.length; i++){
//             if(likeArr[i].opacity <= 0){
//                 d.body.removeChild(likeArr[i].el);  //将div删除
//                 likeArr.splice(i, 1);
//             }

//             likeArr[i].opacity -= 0.01;
//             likeArr[i].scale += 0.01;
//             likeArr[i].top --;
//             // 将属性添加到div的css中
//             likeArr[i].el.style.cssText = `
//                 opacity: ${likeArr[i].opacity};
//                 top: ${likeArr[i].top}px;
//                 left: ${likeArr[i].left}px;
//                 color: ${likeArr[i].color};
//                 transform: scale(${likeArr[i].scale};
//             `
//         }

//         // 动画刷新频率
//         w.requestAnimationFrame(moveLike);
//     }

// })(window, document);

(function(w, d){
    // 添加监听body
    d.querySelector("body").addEventListener('click', function(e){
        addLike(e);
    });

    var likeArr = [];   //like队列
    function addLike(e){
        var likeDiv = d.createElement("div");
        likeDiv.classList.add("like");
        likeDiv.innerHTML = '<i class="fas fa-heart"></i>';
        d.body.appendChild(likeDiv);

        // 每点击一次添加一个like对象
        likeArr.push({
            el: likeDiv,
            top: e.clientY -20,
            left: e.clientX -10, 
            opacity: 1,
            scale: 1,
            color: `rgb(${255*Math.random()},${255*Math.random()},${255*Math.random()} )`
        });

        moveLike();
    }

    function moveLike(){
        for(var i=0; i<likeArr.length; i++){
            if(likeArr[i].opacity <= 0){
                d.body.removeChild(likeArr[i].el);
                likeArr.splice(i, 1);

                return ;
            }

            likeArr[i].top --;
            likeArr[i].opacity -= 0.01;
            likeArr[i].scale += 0.01;
            // 在div源中添加style样式
            // likeArr[i].el.style.cssText = "top: ${likeArr[i].top}px;
            // left: ${likeArr[i].left}px;
            // color: ${likeArr[i].color};
            // opacity: ${likeArr[i].opacity};
            // transform: scale(${likeArr[i].scale});"

            //  ES6的写法，使用反`引导，可以使用${}对势力进行引用
            likeArr[i].el.style.cssText = `
            top: ${likeArr[i].top}px;
            left: ${likeArr[i].left}px;
            color: ${likeArr[i].color};
            opacity: ${likeArr[i].opacity};
            transform: scale(${likeArr[i].scale});`
            
        }

        // 请求动画帧，以屏幕刷新率为准，一般是每秒60帧左右
        w.requestAnimationFrame(moveLike);
    }
})(window, document);
