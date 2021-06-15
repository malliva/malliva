import React from 'react';

import { createAsyncThunk } from '@reduxjs/toolkit';

/* eslint-disable-next-line */
export interface SharedAccountSynApiProps {}

export type SignInError = any;

export interface SignUpState {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
}

export interface SignInState {
  login: {
    email: string;
    password: string;
  };
  token: string;
  authorised: boolean;
  error: SignInError;
}

const API_URL = 'http://localhost:8000/';

export function SharedAccountSynApi(props: SharedAccountSynApiProps) {
  return;
}

export const postSignUpUser = createAsyncThunk(
  'malliva/register',
  async (payload: SignUpState) => {
    const response = await fetch(API_URL + 'api/v1/users/register', {
      body: JSON.stringify(payload),
      method: 'POST',
      mode: 'no-cors',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        if (response) {
          console.error('Error:', response);
          const serverResponse = response.json();
          return { serverResponse };
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        return response.json();
      });
  }
);

export const getSingInUser = createAsyncThunk(
  'malliva/login',
  async (payload: SignInState) => {
    const response = await fetch(
      API_URL + 'api/v1/users/login' + JSON.stringify(payload.login)
    );
    if (response.ok) {
      const serverResponse = response.json();
      return { serverResponse };
    }
    return response.json();
  }
);
