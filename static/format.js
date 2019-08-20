$(document).ready(function() {
   $("input[type=radio]").click(() => {
      const abc= $("input[name=etat]:checked").val();
      if (abc == "Ancien"){
         document.getElementById("matricule").disabled =false;
         document.getElementById("matricule").value ="";
      }
      else{
         document.getElementById("matricule").disabled =true;
         document.getElementById("matricule").value ="{{matricule}}";
      }
     
   }
)});
   