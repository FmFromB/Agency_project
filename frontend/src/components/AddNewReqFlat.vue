<template>
    <div class="border rounded p-3 mx-auto form_reg">
        <b-form @submit="register">
            <div class="form-group">
                <label for="minRooms">Minimal nuber of rooms</label>
                <b-input v-model="minRooms" type="text" id="minRooms" placeholder="min. number of rooms"></b-input>
            </div>
            <div class="form-group">
                <label for="minRooms">Maximum nuber of rooms</label>
                <b-input v-model="maxRooms" type="text" id="maxRooms" placeholder="max. number of rooms"></b-input>
            </div>
            <div class="form-group">
                <label for="minRooms">Minimal floor</label>
                <b-input v-model="minFloor" type="text" id="minFloor" placeholder="minimal floor"></b-input>
            </div>
            <div class="form-group">
                <label for="minRooms">Maximum floor</label>
                <b-input v-model="maxFloor" type="text" id="maxFloor" placeholder="maximum floor"></b-input>
            </div>
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
                minRooms: "",
                maxRooms: "",
                minFloor: "",
                maxFloor: "",
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