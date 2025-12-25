let telegram_id = localStorage.getItem("tid");

async function login(){
  let email = email.value;
  let password = document.getElementById("password").value;

  let r = await fetch("/login?email="+email+"&password="+password,{method:"POST"});
  let d = await r.json();

  if(d.telegram_id){
    localStorage.setItem("tid", d.telegram_id);
    location.href = "/dashboard";
  } else {
    msg.innerText = "Login failed";
  }
}

async function generate(service){
  let r = await fetch(`/generate/${service}`);
  let d = await r.json();
  alert(d.generated || "Error");
}

async function loadAnalytics(){
  let adminId = prompt("Enter Admin Telegram ID");
  let r = await fetch(`/admin/analytics/${adminId}`);
  let d = await r.json();
  out.innerText = JSON.stringify(d,null,2);
}

function checkout(){
  location.href = "https://t.me/Bkdmbot";
}
