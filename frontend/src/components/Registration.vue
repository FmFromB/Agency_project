<template>
    <div class="border rounded p-3 mx-auto form_reg">
        <b-form @submit="register">
            <div class="form-group">
                <label for="first_name">Имя</label>
                <b-input v-model="first_name" type="text" id="first_name" placeholder="Имя"></b-input>
            </div>
            <div class="form-group">
                <label for="last_name">Фамилия</label>
                <b-input v-model="last_name" type="text" id="last_name" placeholder="Фамилия"></b-input>
            </div>
            <div class="form-group">
                <label for="middle_name">Отчество</label>
                <b-input v-model="middle_name" type="text" id="middle_name" placeholder="Отчество"></b-input>
            </div>
            <div class="form-group">
                <label for="phone_number">Номер телефона:</label>
                <b-input v-model="phone_number" type="text" id="phone_number" placeholder="+7 (921) 123 45 67"></b-input>
            </div>
            <div class="form-group">
                <label for="username">Логин</label>
                <b-input v-model="username" type="text" id="username" placeholder="логин"></b-input>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <b-input v-model="email" type="text" id="email" placeholder="example@example.com"></b-input>
            </div>
            <div class="form-group">
                <label for="password">Пароль:</label>
                <b-input v-model="password" type="password" id="password" placeholder="Пароль..."></b-input>
            </div>
            <div class="form-group">
                <label for="repeatPassword">Повторите пароль:</label>
                <b-input v-model="repeatPassword" type="password" id="repeatPassword" placeholder="Повторите пароль..."></b-input>
            </div>
            <b-button variant="primary" type="submit">Регистрация</b-button>
            <p class="mt-3">
                Уже есть аккаунт? <router-link to="/Enterance">Вход</router-link>
            </p>
        </b-form>
    </div>
</template>
<script>
    export default {
        name: "SignUp",
        data() {
            return {
                username: "",
                first_name: "",
                last_name: "",
                middle_name: "",
                password: "",
                repeatPassword: "",
                phone_number: "",
                email: "",
            };
        },
        methods: {
            register(event) {
                event.preventDefault();
                this.axios
                    .post(`http://127.0.0.1:8000/api/auth/users/`, { 'username': this.username, 'password': this.password, 'email': this.email })
                    .then(response => { console.log(response); this.setLogined(response.data.token) })
                    .catch(err => { console.error(err) }) 
                // логика регистрации
            }
        }
    };
</script>