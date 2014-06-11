function addArticleToInvoice(divName, invoicePrefix)
{
    var newdiv = document.createElement('div');
    var number=document.getElementsByName(invoicePrefix + "-NumberOfArticles")[0];
    number.value++;
    var formExample=document.getElementById('example');
    newdiv.innerHTML = formExample.innerHTML.replace(/__NUMBER__/g, number.value);
    document.getElementById(divName).appendChild(newdiv);
}
