//封装函数，获取元素节点
function $(tagName,index){
    if(index){//index非0值时
        var res = document.getElementsByTagName(tagName)[index]
    }else{//index:undefined/0
        var res = document.getElementsByTagName(tagName)[0];
    }
    //返回元素节点对象
    return res;
}
