function addArticleToInvoice(divName, invoicePrefix)
{
    var number=document.getElementById("id_"+invoicePrefix + "-NumberOfArticles");
    number.value++;
    var formExample=document.getElementById('example');
    var newarticle=document.createElement("div");
    newarticle.id="article_"+number.value;
    newarticle.innerHTML = formExample.innerHTML.replace(/__NUMBER__/g, number.value);
    document.getElementById(divName).appendChild(newarticle);
}

function delArticleFromInvoice(articleId, invoicePrefix)
{
    var number=document.getElementById("id_"+invoicePrefix + "-NumberOfArticles");
    number.value--;

    var last=document.getElementById(articleId).children[number.value];
    last.parentNode.removeChild(last);
}
