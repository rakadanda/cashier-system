<template>
  <div class="login-container">
    <Card class="login-card">
      <template #title>Cashier System Login</template>
      <template #content>
        <div class="p-fluid">
          <div class="p-field">
            <label for="email">Email</label>
            <InputText id="email" v-model="email" type="email" />
          </div>
          <div class="p-field">
            <label for="password">Password</label>
            <Password id="password" v-model="password" toggleMask />
          </div>
          <Button 
            label="Login" 
            @click="handleLogin" 
            :loading="loading" 
            class="p-button-raised"
          />
        </div>
      </template>
    </Card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import Card from 'primevue/card'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import { useToast } from 'primevue/usetoast'

const email = ref('')
const password = ref('')
const loading = ref(false)
const router = useRouter()
const authStore = useAuthStore()
const toast = useToast()

const handleLogin = async () => {
  loading.value = true
  try {
    await authStore.login(email.value, password.value)
    toast.add({
      severity: 'success',
      summary: 'Login Success',
      detail: 'Redirecting to dashboard...',
      life: 3000
    })
    router.push(authStore.user.role === 'admin' ? '/admin' : '/cashier')
  } catch (error) {
    toast.add({
      severity: 'error',
      summary: 'Login Failed',
      detail: error.message,
      life: 3000
    })
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}
.login-card {
  width: 400px;
}
.p-field {
  margin-bottom: 1.5rem;
}
</style>
