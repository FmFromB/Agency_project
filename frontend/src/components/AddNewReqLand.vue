<template>
    <div class="border rounded p-3 mx-auto form_reg">
        <b-form @submit="register">
            <div class="form-group">
                <label for="minArea">Minimal area</label>
                <b-input v-model="minArea" type="text" id="minArea" placeholder="min. area"></b-input>
            </div>
            <div class="form-group">
                <label for="maxArea">Maximum area</label>
                <b-input v-model="maxArea" type="text" id="maxArea" placeholder="max. area"></b-input>
            </div>
            <div class="form-group">
                <label for="minPrice">Minimal price</label>
                <b-input v-model="minPrice" type="text" id="minPrice" placeholder="Min. price"></b-input>
            </div>
            <div class="form-group">
                <label for="maxPrice">Maximum price</label>
                <b-input v-model="maxPrice" type="text" id="maxPrice" placeholder="Max. price"></b-input>
            </div>
            <b-button variant="primary" type="submit">Add new requirement</b-button>
        </b-form>
    </div>
</template>
<script>
    export default {
        name: "SignUp",
        data() {
            return {
                minArea: "",
                maxArea: "",
                minPrice: "",
                maxPrice: "",
            };
        },
        methods: {

        }
    };
</script>