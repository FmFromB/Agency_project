<template>
    <div class="border rounded p-3 mx-auto form_reg">
        <b-form @submit="register">
            <div class="form-group">
                <label for="rooms">Rooms</label>
                <b-input v-model="rooms" type="text" id="rooms" placeholder="Rooms"></b-input>
            </div>
            <div class="form-group">
                <label for="floor">Floor</label>
                <b-input v-model="floor" type="text" id="floor" placeholder="Floor"></b-input>
            </div>
            <div class="form-group">
                <label for="area">Area</label>
                <b-input v-model="area" type="text" id="area" placeholder="Area"></b-input>
            </div>
            <div class="form-group">
                <label for="adress">Adress</label>
                <b-input v-model="adress" type="text" id="adress" placeholder="Adress"></b-input>
            </div>
            <div class="form-group">
                <label for="price">Price</label>
                <b-input v-model="price" type="text" id="price" placeholder="Price"></b-input>
            </div>
            <b-button variant="primary" type="submit">Add new flat</b-button>
        </b-form>
    </div>
</template>
<script>
    export default {
        name: "SignUp",
        data() {
            return {
                rooms: "",
                floor: "",
                area: "",
                adress: "",
                price: "",
            };
        },
        methods: {

        }
    };
</script>