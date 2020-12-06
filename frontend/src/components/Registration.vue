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
          <input v-model="formReg.name" type="text" class="form-control" id="name"/>
        </div>
        <div class="form-group">
          <label for="surname">Ваша фамилия</label>
          <input v-model="formReg.surname" type="text" class="form-control" id="surname"/>
        </div>
        <div class="form-group">
          <label for="middlename">Ваше отчество</label>
          <input v-model="formReg.middlename" type="text" class="form-control" id="middlename"/>
        </div>
        <div class="form-group">
          <label for="Pass">Номер телефона</label>
          <input @blur="$v.formReg.phone.$touch()" :class="{'is-invalid': $v.formReg.phone.$error}" v-model="formReg.phone" type="phone" class="form-control" id="phone"/>
          <div v-if="!$v.formReg.phone.required" class="invalid-feedback">
            Пожалйста, введите номер телефона
          </div>
          <div v-if="!$v.formReg.phone.minLength" class="invalid-feedback">
            Номер телефона должен содержать минимум 6 символов
          </div>
        </div>
        <div class="form-group">
          <label for="Email">Email</label>
          <input @blur="$v.formReg.Email.$touch()" :class="{'is-invalid': $v.formReg.Email.$error}" v-model="formReg.Email" type="text" class="form-control" id="Email"/>
          <div v-if="!$v.formReg.Email.required" class="invalid-feedback">
            Пожалуйста, введите вашу почту
          </div>
          <div v-if="!$v.formReg.Email.email" class="invalid-feedback">
            Это поле должно содержать только электронную почту
          </div>
        </div>
        <button @click="nextStep" :disabled="disabledBtn1" type="button" class="btn btn-light">Продолжить</button>
      </div>
      <transition name="slide-fade">
        <div v-show="step === 3" class="step custom-container col-sm-5 mx-auto">
          <div class="form-group">
            <label for="Pass">Пароль</label>
            <input @blur="$v.formReg.Pass.$touch()" :class="{'is-invalid': $v.formReg.Pass.$error}" v-model="formReg.Pass" type="password" class="form-control" id="Pass"/>
            <div v-if="!$v.formReg.Pass.required" class="invalid-feedback">
              Пожалуйста, введите пароль
            </div>
            <div v-if="!$v.formReg.Pass.minLength" class="invalid-feedback">
              Пароль должен содеражить минимум 6 символов
            </div>
          </div>
          <div class="form-group">
            <label for="PassConf">Подтвердите пароль</label>
            <input @blur="$v.formReg.PassConf.$touch()" :class="{'is-invalid': $v.formReg.PassConf.$error}" v-model="formReg.PassConf" type="password" class="form-control" id="PassConf"/>
            <div v-if="!$v.formReg.PassConf.required" class="invalid-feedback">
              Пожалуйста, подтвержите пароль
            </div>
            <div v-if="!$v.formReg.PassConf.sameAs" class="invalid-feedback">
              Пароли должны совпадать
            </div>
          </div>
          <button @click="backStep" type="button" class="btn btn-light mr-2">Back</button>
          <button @click="nextStep" :disabled="disabledBtn2" type="button" class="btn btn-light">Continue</button>
        </div>
      </transition>
      <transition name="slide-fade">
        <div v-show="step === 4" class="step custom-container col-sm-6 mx-auto">
           <h1>Регистрация прошла успешно</h1>
        </div>
      </transition>
    </form>
    <form  @submit.prevent="register">
      <div v-show="step === 5" class="step custom-container col-sm-5 mx-auto">
        <div class="form-group">
          <label for="name2">Ваше имя</label>
          <input @blur="$v.formReg.name2.$touch()" :class="{'is-invalid': $v.formReg.name2.$error}" v-model="formReg.name2" type="text" class="form-control" id="name2"/>
          <div v-if="!$v.formReg.name2.required" class="invalid-feedback">
            Пожалуйста, введите ваше имя
          </div>
        </div>
        <div class="form-group">
          <label for="surname2">Ваша фамилия</label>
          <input @blur="$v.formReg.surname2.$touch()" :class="{'is-invalid': $v.formReg.surname2.$error}" v-model="formReg.surname2" type="text" class="form-control" id="surname2"/>
          <div v-if="!$v.formReg.surname2.required" class="invalid-feedback">
             Пожалуйста, введите вашу фамилию
          </div>
        </div>
        <div class="form-group">
          <label for="middlename2">Ваше отчество</label>
          <input @blur="$v.formReg.middlename2.$touch()" :class="{'is-invalid': $v.formReg.middlename2.$error}" v-model="formReg.middlename2" type="text" class="form-control" id="middlename2"/>
          <div v-if="!$v.formReg.middlename2.required" class="invalid-feedback">
            Пожалуйста, введите ваше отчество
          </div>
          </div>
        <div class="form-group">
          <label for="commission">Ваша желаемая комиссия</label>
          <input v-model="formReg.commission" type="text" class="form-control" id="commission"/>
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
                formReg: {
                    name: '',
                    name2: '',
                    surname: '',
                    surname2: '',
                    middlename: '',
                    middlename2: '',
                    commission: '',
                    phone: '',
                    Email: '',
                    Pass: '',
                    PassConf: '',
                }
            }
        },
        computed: {
            disabledBtn1() {
               return this.$v.formReg.Email.$invalid || this.$v.formReg.phone.$invalid 
            },
            disabledBtn2() {
                return this.$v.formReg.Pass.$invalid || this.$v.formReg.PassConf.$invalid
            },
            disabledBtn3() {
                return this.$v.formReg.name2.$invalid || this.$v.formReg.surname2.$invalid || this.$v.formReg.middlename2.$invalid
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
            }
        },
        validations: {
            formReg: {
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
                Email: {
                    required,
                    email
                },
                Pass: {
                    required,
                    minLength: minLength(6)
               
                },
                PassConf: {
                    required,
                    sameAs: sameAs('Pass')
                },
            }
        }
    }
</script>