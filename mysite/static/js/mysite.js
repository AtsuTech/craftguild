
// console.log('Hello from your_script.js!');

const reservation_form = document.getElementById("reservation");

reservation_form.onsubmit = function(e){

    //フォーム送信による画面更新を無効
    e.preventDefault();

    //フォームから入力内容取得
    const child_name1 = reservation_form.child_name1.value;
    const child_name2 = reservation_form.child_name2.value;
    const parent_name1 = reservation_form.parent_name1.value;
    const parent_name2 = reservation_form.parent_name2.value;
    const email = reservation_form.email.value;
    const phone_number = reservation_form.phone_number.value;
    const schedule = reservation_form.schedule.value;
    const schedule_text = reservation_form.querySelector('input[name="schedule"]:checked').getAttribute('data-schedule');
    const content = reservation_form.content.value;
    const content_text = reservation_form.querySelector('input[name="content"]:checked').getAttribute('data-content');
    const comment = reservation_form.comment.value;

    reservation_form.style.display = "none";
    

    //確認画面に値を渡す
    document.getElementById("confirm_child_name1").textContent = child_name1;
    document.getElementById("child_name1").value = child_name1;

    document.getElementById("confirm_child_name2").textContent = child_name2;
    document.getElementById("child_name2").value = child_name2;

    document.getElementById("confirm_parent_name1").textContent = parent_name1;
    document.getElementById("parent_name1").value = parent_name1;

    document.getElementById("confirm_parent_name2").textContent = parent_name2;
    document.getElementById("parent_name2").value = parent_name2;

    document.getElementById("confirm_email").textContent = email;
    document.getElementById("email").value = email;

    document.getElementById("confirm_phone_number").textContent = phone_number;
    document.getElementById("phone_number").value = phone_number;

    document.getElementById("confirm_schedule").textContent = schedule_text;
    document.getElementById("schedule").value = schedule;

    document.getElementById("confirm_content").textContent = content_text;
    document.getElementById("content").value = content;

    document.getElementById("confirm_comment").textContent = comment;
    document.getElementById("comment").value = comment;


}