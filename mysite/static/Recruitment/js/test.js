function AdaptionDevice(){
	var w = document.documentElement.clientWidth;
	var h = document.documentElement.clientHeight;
	
	var hs = screen.height;
	
	var nvg = document.getElementById('nv-on-pc');
	var logbtn = document.getElementById('login-btn')
	var morebntn = document.getElementById('more-info');
	var sech = document.getElementById('sech');
	
	
	if(w<1200){
		nvg.style.display = "none";
		logbtn.style.display = "none";
		morebntn.style.display = "block"
		sech.style.display="none"
		if(w < 576){
			var bg = document.getElementById("home-bg");
			bg.src = "/static/Recruitment/img/mobile-banner.gif";

			var vidplayer = document.getElementById("vid-show");

			vidplayer.style.top = "800px";

			var vide = vidplayer.children[2];

			vide.style.width = "100%";

			vide.style.height = "100%";

			vide.style.marginTop = "3em"

			var closebtn = document.getElementById('closebtn');

			var openbtn = document.getElementById('openbtn');


			closebtn.style.marginLeft = "90%"
			openbtn.style.marginLeft = "90%"

			closebtn.style.marginTop = "3em";
			openbtn.style.marginTop = "3em";
		}
	}
	else
	{
		nvg.style.display = "block";
		logbtn.style.display = "block";
		morebntn.style.display = "none";
		sech.style.display = "flex";
		
		var bg = document.getElementById("home-bg");
		bg.src = "/static/Recruitment/img/new-home-banner.gif";
		
		var vidplayer = document.getElementById("vid-show");
		
		vidplayer.style.top = "900px";
		
		var vide = vidplayer.children[1];
		
		vide.style.width = "60%";
		
		vide.style.height = "60%";

		vide.style.marginTop = "20em"

			var closebtn = document.getElementById('closebtn');

			var openbtn = document.getElementById('openbtn');


			closebtn.style.marginLeft = "76.5%"
			openbtn.style.marginLeft = "76.5%"

			closebtn.style.marginTop = "21em";
			openbtn.style.marginTop = "21em";
		
		console.log();
		
		// if(w < )
		// var closebtn = 
	}
	
}



window.addEventListener('resize',AdaptionDevice);
AdaptionDevice();

function screenAdaption(){
	

}
// screenAdaption();

var openbtn = document.getElementById("openbtn");

var closebtn = document.getElementById("closebtn");

function playVdAudio(){
	
	
	console.log(event.target.getBoundingClientRect());
	
}

// var tesbtn = document.getElementById("testbtn");

function openVoice(){
	var vedio = document.getElementById('vd');

	var closebtn = document.getElementById('closebtn');

	var openbtn = document.getElementById('openbtn');

	// vedio.removeAttribute("muted");
	vedio.muted = false;
	closebtn.style.display = "block";

	openbtn.style.display = "none";
}

function  closeVoice() {
	var vedio = document.getElementById('vd');

	var closebtn = document.getElementById('closebtn');

	var openbtn = document.getElementById('openbtn');

	// vedio.setAttribute("muted","");
	vedio.muted = true;
	closebtn.style.display = "none";

	openbtn.style.display = "block";
}


function setPagination(page_cnt){

	var paginationGrp = document.getElementsByClassName('linkt text-decoration-none');



		var url = window.location.href;

		var url_info = url.split("/");

		var now_page = url_info[url_info.length - 2];

		// console.log(typeof now_page);

		var preomit = document.getElementById('pre');
		var nextomit = document.getElementById('next');



		var pre_page = page_num - 1;

		var next_page = page_num + 1

		// preomit.children[0].href = "/jobs/" + pre_page + "/";
		// nextomit.children[0].href = "/jobs/" + next_page + "/";

		// preomit.style.display = "block";
		// nextomit.style.display = "block";
		if(now_page == 1)
		{
			preomit.style.display = "none";

		}
		if(now_page == page_cnt){

			nextomit.style.display = "none";
		}



		if(page_num > 3 && page_num < page_cnt - 2){

			paginationGrp[1].children[1].innerHTML = "";

			paginationGrp[3].children[0].style.display = "block";
			paginationGrp[1].children[0].style.display = "block";
			paginationGrp[3].setAttribute('disabled','');
			paginationGrp[1].setAttribute('disabled','');

			paginationGrp[2].innerHTML = now_page;

			paginationGrp[2].href = "/jobs/" + now_page + "/";

		}
		else if(page_num <= 3){
			// console.log();
		paginationGrp[1].children[0].style.display = "none";
		// paginationGrp[3].setAttribute('disabled','');
		// paginationGrp[3].children[0].style.display = "block";
		paginationGrp[1].children[1].innerHTML = "2";
		}
		else if (page_num >= page_cnt - 2){
			paginationGrp[3].children[0].style.display = "none";

			// paginationGrp[1].innerText = "";
			paginationGrp[1].children[1].innerHTML = "";
			paginationGrp[1].children[0].style.display = "block";
			// paginationGrp[1].setAttribute('disabled','');

			paginationGrp[3].children[1].innerHTML = page_cnt - 1;
			paginationGrp[3].href = "/jobs/" + (page_cnt - 1) + "/";
			paginationGrp[2].innerHTML = page_cnt - 2;

			paginationGrp[2].href = "/jobs/" + (page_cnt - 2) + "/";


		}


		var cardlist = document.getElementsByClassName('card shadow-sm');

		var id_list = document.getElementsByClassName('breadcrumb-item active job-id');

		for(i = 0; i < cardlist.length; i ++){

			cardlist[i].children[0].href = "/" + id_list[i].innerText +"/details/";

		}
}

window.onload = setPagination;



// window.onload = showJobst;
//
// function next_page(){
//
// }

