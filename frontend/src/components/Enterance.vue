<template>
    <div class="mx-auto border p-3 rounded custom-container light">
        <b-form @submit="login">
            <div class="form-group">
                <label for="username">Email:</label>
                <b-input v-model="email" type="text" id="username" placeholder="example@mail.com"></b-input>
            </div>
            <div class="form-group">
                <label for="password">Пароль:</label>
                <b-input v-model="password" type="password" id="password" placeholder="Пароль..."></b-input>
            </div>
            <b-button variant="primary" type="submit">Войти</b-button>
            <p class="mt-3">
                Ещё не зарегистрированы? <router-link to="/Registration">Регистрация</router-link>
            </p>
        </b-form>
    </div>
</template>
<script>
    export default {
        name: "SignIn",
        data() {
            return {


                email: "",
                password: ""
            };
        },
        methods: {
            login(event) {
                event.preventDefault();
                this.axios
                    .post(`http://localhost:8000/api/auth/token/`, { 'email': this.email, 'password': this.password })
                    .then(response => { this.setLogined(response.data.token) })
                    .catch(err => { console.error(err) })
                // логика авторизации
            },
        }
    };
</script>
