
    window.addEventListener('scroll',reveal);
    function reveal(){
        var r = document.querySelectorAll('.rev'); 

        for(var i=0;i<r.length;i++){
            var whe = window.innerHeight;
            var rtop = r[i].getBoundingClientRect().top;
            var point =150;

            if(rtop < (whe-point) ){
                r[i].classList.add('active'); 
            }
            else{
                r[i].classList.remove('active'); 
            }

        }
    }
    

    