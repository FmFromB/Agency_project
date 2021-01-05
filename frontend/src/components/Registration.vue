<template>
  <div class="form_reg">
    <div v-show="step === 1">
      <div class ="text">
        <h1>Вы хотите зарегистрироваться как</h1>
      </div>
      <div class="buttons">
        <div class="button1">
          <b-button variant="light" size="lg" @click="clientReg" type="button" class="btn btn-light col-sm-6">Клиент</b-button>
        </div>
        <div>
          <b-button variant="light" size="lg" @click="realtorReg" type="button" class="btn btn-light col-sm-6">Риэлтор</b-button>
        </div>
      </div>
    </div>
    <form @submit.prevent="register">
      <div v-show="step === 2" class="step custom-container col-sm-5 mx-auto">
        <div class="form-group">
          <label for="name">Ваше имя</label>
          <input v-model="name" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="surname">Ваша фамилия</label>
          <input v-model="surname" type="text" class="form-control" id="surname"/>
        </div>
        <div class="form-group">
          <label for="middlename">Ваше отчество</label>
          <input v-model="middlename" type="text" class="form-control" id="middlename"/>
        </div>
        <div class="form-group">
          <label for="password">Номер телефона</label>
          <input @blur="$v.phone.$touch()" :class="{'is-invalid': $v.phone.$error}" v-model="phone" type="phone" class="form-control" id="phone"/>
          <div v-if="!$v.phone.required" class="invalid-feedback">
            Пожалйста, введите номер телефона
          </div>
          <div v-if="!$v.phone.minLength" class="invalid-feedback">
            Номер телефона должен содержать минимум 6 символов
          </div>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input @blur="$v.email.$touch()" :class="{'is-invalid': $v.email.$error}" v-model="email" type="text" class="form-control" id="email"/>
          <div v-if="!$v.email.required" class="invalid-feedback">
            Пожалуйста, введите вашу почту
          </div>
          <div v-if="!$v.email.email" class="invalid-feedback">
            Это поле должно содержать только электронную почту
          </div>
        </div>
        <button @click="nextStep" :disabled="disabledBtn1" type="button" class="btn btn-light">Продолжить</button>
      </div>
      <transition name="slide-fade">
        <div v-show="step === 3" class="step custom-container col-sm-5 mx-auto">
          <div class="form-group">
            <label for="password">Пароль</label>
            <input @blur="$v.password.$touch()" :class="{'is-invalid': $v.password.$error}" v-model="password" type="password" class="form-control" id="password"/>
            <div v-if="!$v.password.required" class="invalid-feedback">
              Пожалуйста, введите пароль
            </div>
            <div v-if="!$v.password.minLength" class="invalid-feedback">
              Пароль должен содеражить минимум 6 символов
            </div>
          </div>
          <div class="form-group">
            <label for="PassConf">Подтвердите пароль</label>
            <input @blur="$v.PassConf.$touch()" :class="{'is-invalid': $v.PassConf.$error}" v-model="PassConf" type="password" class="form-control" id="PassConf"/>
            <div v-if="!$v.PassConf.required" class="invalid-feedback">
              Пожалуйста, подтвержите пароль
            </div>
            <div v-if="!$v.PassConf.sameAs" class="invalid-feedback">
              Пароли должны совпадать
            </div>
          </div>
          <button @click="backStep" type="button" class="btn btn-light mr-2">Back</button>
          <button @click="signup" :disabled="disabledBtn2" type="button" class="btn btn-light">Зарегестрироваться</button>
        </div>
      </transition>
    </form>
    <form  @submit.prevent="register">
      <div v-show="step === 5" class="step custom-container col-sm-5 mx-auto">
        <div class="form-group">
          <label for="name2">Ваше имя</label>
          <input @blur="$v.name2.$touch()" :class="{'is-invalid': $v.name2.$error}" v-model="name2" type="text" class="form-control" id="name2"/>
          <div v-if="!$v.name2.required" class="invalid-feedback">
            Пожалуйста, введите ваше имя
          </div>
        </div>
        <div class="form-group">
          <label for="surname2">Ваша фамилия</label>
          <input @blur="$v.surname2.$touch()" :class="{'is-invalid': $v.surname2.$error}" v-model="surname2" type="text" class="form-control" id="surname2"/>
          <div v-if="!$v.surname2.required" class="invalid-feedback">
             Пожалуйста, введите вашу фамилию
          </div>
        </div>
        <div class="form-group">
          <label for="middlename2">Ваше отчество</label>
          <input @blur="$v.middlename2.$touch()" :class="{'is-invalid': $v.middlename2.$error}" v-model="middlename2" type="text" class="form-control" id="middlename2"/>
          <div v-if="!$v.middlename2.required" class="invalid-feedback">
            Пожалуйста, введите ваше отчество
          </div>
          </div>
        <div class="form-group">
          <label for="commission">Ваша желаемая комиссия</label>
          <input v-model="commission" type="text" class="form-control" id="commission"/>
        </div>
        <button @click="passwordStep" :disabled="disabledBtn3" type="button" class="btn btn-light">Continue</button>
      </div>
    </form>
  </div>
</template>
<script>
    import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'
    export default {
        data() {
            return {
                step: 1,
                name: null,
                name2: '',
                surname: '',
                surname2: '',
                middlename: '',
                middlename2: '',
                commission: '',
                phone: '',
                email: null,
                password: null,
                PassConf: '',
            }
        },
        computed: {
            disabledBtn1() {
               return this.$v.email.$invalid || this.$v.phone.$invalid 
            },
            disabledBtn2() {
                return this.$v.password.$invalid || this.$v.PassConf.$invalid
            },
            disabledBtn3() {
                return this.$v.name2.$invalid || this.$v.surname2.$invalid || this.$v.middlename2.$invalid
            }
        },
        methods: {
            nextStep() {
                if (this.step < 100) {
                    this.step++
                }
            },
            backStep() {
                if (this.step > -100) {
                    this.step--
                }
            },
            clientReg() {
              this.step = 2 
            },
            realtorReg() {
              this.step = 5
            },
            passwordStep() {
              this.step = 3
            },
            signup() {
              this.$store.dispatch('SIGNUP', {name:this.name, surname:this.surname, middlename:this.middlename, phone:this.phone, email:this.email, password:this.password})
            }
        },
        validations: {
   
                name: {},
                name2: {
                    required,
                },
                surname: {},
                surname2: {
                    required
                },
                middlename: {},
                middlename2: {
                    required
                },
                commission: {},
                phone: {
                    required,
                    minLength: minLength(6)
                },
                email: {
                    required,
                    email
                },
                password: {
                    required,
                    minLength: minLength(6)
               
                },
                PassConf: {
                    required,
                    sameAs: sameAs('password')
                },
        }
    }
</script>