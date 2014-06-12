function addArticleToInvoice(divName, invoicePrefix)
{
    var number=document.getElementById("id_"+invoicePrefix + "-NumberOfArticles");
    number.value++;
    var formExample=document.getElementById('example');
    var newarticle=document.createElement("div");
    newarticle.id="article_"+number.value+"-div";
    newarticle.innerHTML = formExample.innerHTML.replace(/__NUMBER__/g, number.value);
    document.getElementById(divName).appendChild(newarticle);
}

function delArticleFromInvoice(articleId, invoicePrefix)
{
    var article=document.getElementById(articleId);
    article.parentNode.removeChild(article);
    document.getElementById("id_"+invoicePrefix + "-NumberOfArticles").value--;
}
