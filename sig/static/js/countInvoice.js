function countWholeInvoice(articlesDivId, nettoId, vatId, bruttoId)
{
    var what=document.getElementById(articlesDivId);

    var sum_netto=0.0, sum_vat=0.0, sum_brutto=0.0;
    for (var i=0; i<what.childElementCount; i++)
    {
        var prefix=what.children[i].id;
        var price=document.getElementById(prefix+'_price').innerHTML;
        var quantity=document.getElementById(prefix+'_quantity').innerHTML;

        var netto=document.getElementById(prefix+'_netto');
        var vat=document.getElementById(prefix+'_vat');
        var brutto=document.getElementById(prefix+'_brutto');
        netto.innerHTML=price*quantity;
        vat.innerHTML=23*price*quantity/100.0;
        brutto.innerHTML=parseFloat(netto.innerHTML)+parseFloat(vat.innerHTML);
        
        sum_netto+=parseFloat(netto.innerHTML);
        sum_vat+=parseFloat(vat.innerHTML);
        sum_brutto+=parseFloat(brutto.innerHTML);
    }

    document.getElementById(nettoId).innerHTML=sum_netto;
    document.getElementById(vatId).innerHTML=sum_vat;
    document.getElementById(bruttoId).innerHTML=sum_brutto;
}
