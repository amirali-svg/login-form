const createAccountRedirectBtn = document.querySelector(
  ".create_account_redirect-btn"
);
const form = document.querySelector(".form");

const changeFormContent = () => {
  form.innerHTML = "";

  form.insertAdjacentHTML(
    "beforeend",
    `<h2 class="form-title">Sign up</h2>
        <div class="form-input-1">
          <label class="form-label" for="text">username</label>
          <br />
          <input class="form-input" type="text" name="uid" id="text" />
        </div>
        <div class="form-input-2">
          <label class="form-label" for="password">password</label>
          <br />
          <input class="form-input" type="password" name="pwd"/>
        </div>

        <div class="h-20 flex justify-center content-center flex-col">
          <label class="form-label" for="password">Email</label>
          <input class="form-input" type="password" name="pwd"/>
        </div>

        <button class="form-submit-btn " type="submit" name="submit">
          Sign up
        </button>`
  );
};

createAccountRedirectBtn.addEventListener("click", changeFormContent);

