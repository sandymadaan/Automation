/* This File Contains Various Validation functions and AJAX Functions
 * The Contents of This file are available under GPL License.
 * Author: Harbhag Singh Sohal
 * Blog : http://harbhag.wordpress.com
 */





function checkbranch(){
	var course=document.getElementById('Course')
	var branch=document.getElementById('Branch')
	if(course.value=='MBA'){
		if(branch.value != ''){
			alert("Please Leave Branch Field Blank for "+course.value);
			return false;
		}
	}
	
	if(course.value=='MCA'){
		if(branch.value != ''){
			alert("Please Leave Branch Field Blank for "+course.value);
			return false;
		}
	}
	
	if(course.value=='B.Tech'){
		if(branch.value=='' || branch.value=='N/A'){
			alert("Please Select Branch");
			return false;
		}
	}
	
}

function confirm_add(){
	var answer = confirm("You are going add new user, do you want to continue ?");
	
	if(answer){
		return true;
	}
	else{
		return false;
	}
}

function confirm_edit(rollno){
	var answer = confirm("You are going to update the entry for Roll No "+ rollno+", do you want to continue ?");
	
	if(answer){
		return true;
	}
	else{
		return false;
	}
}

function confirm_delete(rollno){
	var answer = confirm("You are going to delete the entry for Roll No "+ rollno+", do you want to continue ?");
	
	if(answer){
		return true;
	}
	else{
		return false;
	}
}

function confirm_delete_user(name){
	var answer = confirm("You are going to delete the User  "+ name+", do you want to continue ?");
	
	if(answer){
		return true;
	}
	else{
		return false;
	}
}

function checkpassword(){
	var password=document.getElementById('New_Password')
	var password_confirm=document.getElementById('Confirm_Password')
	
	if(password.value==''){
		alert("Please Enter Password");
		return false;
	}
	
	if(password.value!=''){
		
		if(password.value!=password_confirm.value){
			alert("Both Passwords Does not Match");
			return false;
		}
	}
}



function add_other_checkpassword(){
	var username = document.getElementById('Username')
	var password=document.getElementById('New_Password')
	var password_confirm=document.getElementById('Confirm_Password')
	var fullname = document.getElementById('Full_Name')
	
	if(username.value=='') {
		alert("Please Enter Username");
		return false;
	}
	
	if(password.value==''){
		alert("Please Enter Password");
		return false;
	}
	
	if(password.value!=''){
		
		if(password.value!=password_confirm.value){
			alert("Both Passwords Does not Match");
			return false;
		}
	}
	
	if(fullname.value=='') {
		alert("Please Enter Fullname");
		return false;
	}
	else {
		var depa = document.getElementById('Department_Ajax').value;
		document.getElementById('Department').value=depa;
	}
}


function change_password_user(current){
	var post=document.getElementById('Current_Password')
	var password=document.getElementById('New_Password')
	var password_confirm=document.getElementById('Confirm_Password')
	if(post.value!=current){
		alert("Wrong Current Password");
		return false;
	}
	
	if(password.value==''){
		alert("Please Enter Password");
		return false;
	}
	
	if(password.value!=''){
		
		if(password.value!=password_confirm.value){
			alert("New Password and Confirm Password Does Not Match");
			return false;
		}
	}
}

function CheckAll(chk){
	var mobile = new Array();
	for (i = 0; i < chk.length; i++){
		chk[i].checked = true ;
	}
}

function UnCheckAll(chk){
	for (i = 0; i < chk.length; i++)
	chk[i].checked = false ;
}

function add_mobile(chk,objid){
	var mobile = new Array();
	for (i = 0; i < chk.length; i++){
		if(chk[i].checked==true){
			mobile.push(chk[i].value);
		}
	}
	mobile_str = mobile.join(",")
	var x = document.getElementById(objid);
	x.value = mobile_str;
}



function disappear_name(id) {
	document.getElementById(id).innerHTML="";
}

function show_name(id,name) {
	document.getElementById(id).innerHTML=name;
}


function changedist(str)
{
if (str=="")
  {
  document.getElementById("dist").innerHTML="";
  return;
  }
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById('dist').innerHTML=xmlhttp.responseText;
    }


}

xmlhttp.open("GET","dist.php?q="+str,true);
xmlhttp.send();
}

function setstate(distr)
{
	var str=document.getElementById('State');
	
	if (str.value=="")
  {
  document.getElementById("dist").innerHTML="";
  return;
  }
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById('dist').innerHTML=xmlhttp.responseText;
    }


}

xmlhttp.open("GET","dist.php?q="+str.value+"&d="+distr,true);
xmlhttp.send();

}

function checkcompany(){
	var company = document.getElementById("Company_Name");
	var other = document.getElementById("Other_Company");
	if(company.value!=''){
		if(other.value!=''){
			alert("Either Select company from Dropdown or Enter name manually. Do not fill both the fields");
			return false;
		}
	}
}

function patience(){
	alert("Sending email to all the students can take upto 10 Mins. so please be patient");
}
		
function admission_no()
{
	var xmlhttp;
	var str=document.getElementById('Admission_Type');
	if (str.value!="PTU Councelling")
  {
  document.getElementById("ad_no").innerHTML="";
  return;
  }
  
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
  
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById('ad_no').innerHTML=xmlhttp.responseText;
    }


}
xmlhttp.open("GET","add_no.php",true);
xmlhttp.send();
	
}



function admission_no_edit(ad_no)
{
	var xmlhttp;
	var str=document.getElementById('Admission_Type');
	if (str.value!="PTU Councelling")
  {
  document.getElementById("ad_no").innerHTML="";
  return;
  }
  
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
  
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById('ad_no').innerHTML=xmlhttp.responseText;
    }


}
xmlhttp.open("GET","add_no.php?q="+ad_no,true);
xmlhttp.send();
	
}




function disappear_ad_no() {
	var str = document.getElementById('Admission_Type');
	if(str.value!="PTU Councelling"){
		disappear_name("ad_no_name");
	document.getElementById("ad_no").innerHTML="";
}
if(str.value=="PTU Councelling"){
	show_name("ad_no_name","Admission No.");
	admission_no();
}

}


function disappear_ad_no_edit() {
	var str = document.getElementById('Admission_Type');
	if(str.value!="PTU Councelling"){
		document.getElementById("ad_no_name").innerHTML="";
		document.getElementById("ad_no").innerHTML="";
}
if(str.value=="PTU Councelling"){
	var no = document.getElementById("ad_no_hidden");
	show_name("ad_no_name","Admission No.");
	admission_no_edit(no.value);
}

}

function set_branch_selector() {
	show_name('branch_div_name','Branch');
		var xmlhttp;
		if (window.XMLHttpRequest)
		{// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
  
		else
		{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				document.getElementById('branch_div').innerHTML=xmlhttp.responseText;
			}


		}		
		xmlhttp.open("GET","branch_selector.php",true);
		xmlhttp.send();
}

function branch_selector(val) {
	if(val=='B.Tech' || val=='M.Tech') {
		show_name('branch_div_name','Branch');
		var xmlhttp;
		if (window.XMLHttpRequest)
		{// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
  
		else
		{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				document.getElementById('branch_div').innerHTML=xmlhttp.responseText;
			}


		}		
		xmlhttp.open("GET","branch_selector.php",true);
		xmlhttp.send();
	
	}
	else {
		document.getElementById("branch_div").innerHTML="";
		disappear_name('branch_div_name');
	}
}

function set_semester_branch_batch() {
	var course = document.getElementById('Course').value;
	var batch = document.getElementById('Batch_Ajax').value;
	if(course=='B.Tech') {
		var branch = document.getElementById('Branch_Ajax').value;
		document.getElementById('Branch').value=branch;
	}
	if(course=='M.Tech') {
		var branch = document.getElementById('Branch_Ajax').value;
		document.getElementById('Branch').value=branch;
	}
	var semester = document.getElementById('Semester_Ajax').value;
	document.getElementById('Batch').value=batch;
	document.getElementById('Semester').value=semester;
}



function batch_selector() {
	var course = document.getElementById('Course').value;
	show_name('batch_div_name','Batch');
		var xmlhttp;
		if (window.XMLHttpRequest)
		{// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
  
		else
		{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				document.getElementById('batch_div').innerHTML=xmlhttp.responseText;
			}


		}		
		xmlhttp.open("GET","batch_selector.php?course="+course,true);
		xmlhttp.send();
}




function set_semester_selector() {
	var dt = new Date();
	if((dt.getMonth()+1)>=7) {
		var batch = dt.getFullYear();
	}
	else {
		var batch = dt.getFullYear()-1;
	}
	var course = document.getElementById('Course').value;
	//alert(batch.length);
	show_name('semester_div_name','Semester');
		var xmlhttp;
		if (window.XMLHttpRequest)
		{// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
  
		else
		{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				document.getElementById('semester_div').innerHTML=xmlhttp.responseText;
			}


		}		
		xmlhttp.open("GET","semester_selector.php?batch="+batch+"&course="+course,true);
		xmlhttp.send();
}



function semester_selector() {
	var batch = document.getElementById('Batch_Ajax').value;
	var course = document.getElementById('Course').value;
	show_name('semester_div_name','Semester');
		var xmlhttp;
		if (window.XMLHttpRequest)
		{// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
  
		else
		{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				document.getElementById('semester_div').innerHTML=xmlhttp.responseText;
			}


		}		
		xmlhttp.open("GET","semester_selector.php?batch="+batch+"&course="+course,true);
		xmlhttp.send();
}


function add_other_admin_department() {
	var val = document.getElementById('usertype').value;
	if(val!='Training And Placement'){
		show_name('department_div_name','Department');
		var xmlhttp;
		if (window.XMLHttpRequest)
		{// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp=new XMLHttpRequest();
		}
  
		else
		{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange=function()
		{
			if (xmlhttp.readyState==4 && xmlhttp.status==200)
			{
				document.getElementById('department_div').innerHTML=xmlhttp.responseText;
			}


		}		
		xmlhttp.open("GET","add_other_admin_department.php",true);
		xmlhttp.send();
	}
	else {
		disappear_name('department_div_name');
		document.getElementById('department_div').innerHTML='';
	}
}

function groupname_selector() {
	show_name('group_div_name','Group');
	var batch = document.getElementById('Batch').value;
	var xmlhttp;
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}
  
	else
	{// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById('group_div').innerHTML=xmlhttp.responseText;
		}


	}		
	xmlhttp.open("GET","batch_selector.php?batch="+batch+"&other=create_groups",true);
	xmlhttp.send();
}

function set_groupname() {
	var groupname = document.getElementById('Group_Name_Ajax').value;
	document.getElementById('Group_Name').value=groupname;
}

function disable_check_group(i_d,total_groups) {
	$info = i_d.split('-');
	var group = $info[0];
	var groupno = $info[1];
	var rollno = $info[2];
	var i_count = parseInt(groupno)+1;
	var ungrouped = document.getElementById('ungrouped').value;
	if(document.getElementById(i_d).checked) {
		document.getElementById('ungrouped').value = parseInt(ungrouped)-1;
	}
	else {
		document.getElementById('ungrouped').value = parseInt(ungrouped)+1;
	}
	for(i_count;i_count<=total_groups;i_count++) {
		if(document.getElementById(group+'-'+i_count+'-'+rollno).disabled) {
			document.getElementById(group+'-'+i_count+'-'+rollno).disabled=false;
		}
		else {
			document.getElementById(group+'-'+i_count+'-'+rollno).disabled=true;
		}
	}
	var i_down = parseInt(groupno)-1;
	if(groupno!='1') {
		for (i_down;i_down>0;i_down--) {
			if(document.getElementById(group+'-'+i_down+'-'+rollno).disabled) {
			document.getElementById(group+'-'+i_down+'-'+rollno).disabled=false;
			}
			else {
				document.getElementById(group+'-'+i_down+'-'+rollno).disabled=true;
			}
		}
	}
	
}


function groupname_selector_edit() {
	show_name('group_div_name','Group');
	var batch = document.getElementById('Batch').value;
	var xmlhttp;
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}
  
	else
	{// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById('group_div').innerHTML=xmlhttp.responseText;
		}


	}		
	xmlhttp.open("GET","batch_selector.php?batch="+batch+"&other=editing",true);
	xmlhttp.send();
}

function check_ungrouped(numgroups,numcheckbox) {
	var count = document.getElementById('ungrouped').value;
	var count_checked = 0;
	
	for(k=1;k<=numgroups;k++) {
		if(document.getElementById('AcademicIncharge'+k).value=='') {
			alert("Please Select Academic Incharge For Group-"+k)
			return false;
		}
	}
	
	if(count!='0') {
		alert("There are still "+count+" students needs to be grouped. Group the remaining students before moving forward.");
		return false;
	}
	
	
	for(i=1;i<=numgroups;i++) {
		count_checked = 0;
		for(j=0;j<=numcheckbox-1;j++) {
			if(document.getElementById('Group'+'-'+i+'-'+j).checked) {
				count_checked += 1;
			}
		
		}
		if(count_checked==0) {
			alert("Group-"+i+" is empty, please add atleast one student.");
			return false;
		}
	}
}


function check_unsubgrouped(numgroups,numcheckbox) {
	var count = document.getElementById('ungrouped').value;
	var count_checked = 0;
	
	for(k=1;k<=numgroups;k++) {
		if(document.getElementById('SubgroupAdvisor'+k).value=='') {
			alert("Please Select Advisor For Subgroup-"+k)
			return false;
		}
	}
	
	
	if(count!='0') {
		alert("There are still "+count+" students needs to be grouped. Group the remaining students before moving forward.");
		return false;
	}
	
	
	for(i=1;i<=numgroups;i++) {
		count_checked = 0;
		for(j=0;j<=numcheckbox-1;j++) {
			if(document.getElementById('Subgroup'+'-'+i+'-'+j).checked) {
				count_checked += 1;
			}
		
		}
		if(count_checked==0) {
			alert("Subgroup-"+i+" is empty, please add atleast one student.");
			return false;
		}
	}
}


function check_edit_unsubgrouped(numgroups,numcheckbox) {
	var count = document.getElementById('ungrouped').value;
	var count_checked = 0;
	
	if(count!='0') {
		alert("There are still "+count+" students needs to be grouped. Group the remaining students before moving forward.");
		return false;
	}
	
	
	for(i=1;i<=numgroups;i++) {
		count_checked = 0;
		for(j=0;j<=numcheckbox-1;j++) {
			if(document.getElementById('Subgroup'+'-'+i+'-'+j).checked) {
				count_checked += 1;
			}
		
		}
		if(count_checked==0) {
			alert("Subgroup-"+i+" is empty, please add atleast one student.");
			return false;
		}
	}
}
