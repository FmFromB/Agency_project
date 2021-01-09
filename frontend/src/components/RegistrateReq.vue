<template>
  <div class="form_reg">
    <form @submit.prevent="register">
      <div v-show="step === 1" class="step custom-container col-sm-5 mx-auto">
        <div class="form-group">
          <label for="name">Минимальная цена</label>
          <input v-model="formReg.minPrice" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="name">Максимальная цена</label>
          <input v-model="formReg.maxPrice" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="name">Минимальная площадь</label>
          <input v-model="formReg.minArea" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="name">Максимальная площадь</label>
          <input v-model="formReg.maxArea" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="name">Минимальное количесво комнат</label>
          <input v-model="formReg.minRooms" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="surname">Максимальное количество комнат</label>
          <input v-model="formReg.maxRooms" type="text" class="form-control" id="surname"/>
        </div>
        <div class="form-group">
          <label for="name">Минимальный этаж</label>
          <input v-model="formReg.minFloor" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="surname">Максимальный этаж</label>
          <input v-model="formReg.maxFloor" type="text" class="form-control" id="surname"/>
        </div>
        <div class="form-group">
          <label for="Pass">Минимальное количество этажей в доме</label>
          <input v-model="formReg.minNumFloors" class="form-control" id="phone"/>
        </div>
        <div class="form-group">
          <label for="Pass">Максимальное количество этажей в доме</label>
          <input v-model="formReg.maxNumFloors" class="form-control" id="phone"/>
        </div>
        <div class="form-group">
          <label for="lang">Тип имущества</label>
          <select v-model="formReg.type" class="form-control custom-select" id="lang">
            <option value="Flat">Квартира</option>
            <option value="House">Дом</option>
            <option value="Land">Земля</option>
          </select>
        </div>
        <button variant="dark" @click="nextStep" type="button" class="btn btn-light">Продолжить</button>
      </div>
      <div v-show="step === 2" class="step custom-container col-sm-6 mx-auto">
        <h1>Регистрация прошла успешно</h1>
      </div>
    </form>
  </div>
</template>
<script>
    import {} from 'vuelidate/lib/validators'
    export default {
        data() {
            return {
                step: 1,
                formReg: {
                    minArea: '',
                    maxArea: '',
                    minRooms: '',
                    maxRooms: '',
                    minFloor: '',
                    maxFloor: '',
                    minNumFloors: '',
                    maxNumFloors: '',
                    type: '',
                    minPrice: '',
                    maxPrice: '',
                }
            }
        },
        computed: {
            disabledBtn1() {
               return this.$v.formReg.Email.$invalid || this.$v.formReg.phone.$invalid 
            },
        },
        methods: {
            nextStep() {
                if (this.step < 3) {
                    this.step++
                }
            },
            backStep() {
                if (this.step > -1) {
                    this.step--
                }
            },
        },
        validations: {
            formReg: {
                minArea: {},
                maxArea: {},
                minRooms: {},
                maxRooms: {},
                minFloor: {},
                maxFloor: {},
                minNumFloors: {},
                maxNumFloors: {},
                type: {},
            }
        }
    }
</script>