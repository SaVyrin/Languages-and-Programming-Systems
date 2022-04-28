const fileSelector = document.getElementById('file-selector');
  fileSelector.addEventListener('change', function(){
    var fr=new FileReader();
            fr.onload=function(){
                document.getElementById('text_to_send')
                        .textContent=fr.result;
            }
              
            fr.readAsText(this.files[0]);

    document.getElementById('uploaded').style.display = "block";
    document.getElementById('not_uploaded').style.display = "none";
    document.getElementById('file_name').textContent = this.files[0].name;

  });