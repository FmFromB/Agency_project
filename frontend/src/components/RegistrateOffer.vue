<template>
  <div class="form_reg">
    <form @submit.prevent="register">
      <div v-show="step === 1" class="step custom-container col-sm-5 mx-auto">
        <div class="form-group">
          <label for="name">Цена</label>
          <input v-model="formReg.price" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="name">Адрес</label>
          <input v-model="formReg.adress" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="name">Этаж</label>
          <input v-model="formReg.floor" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="surname">Количество комнат</label>
          <input v-model="formReg.rooms" type="text" class="form-control" id="surname"/>
        </div>
        <div class="form-group">
          <label for="middlename">Площадь</label>
          <input v-model="formReg.area" type="text" class="form-control" id="middlename"/>
        </div>
        <div class="form-group">
          <label for="Pass">Общее количество этажей в доме</label>
          <input v-model="formReg.all_layers" class="form-control" id="phone"/>
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
                    price: '',
                    adress: '',
                    floor: '',
                    area: '',
                    rooms: '',
                    all_layers: ''
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
                adress: {},
                floor: {},
                rooms: {},
                area: {},
                all_floors: {},
                type: {},
            }
        }
    }
</script>