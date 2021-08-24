import {
  signInSliceReducer,
  SIGNIN_USER_KEY,
} from '@client/market-app/sign-in';

import {
  SIGNUP_USER_KEY,
  signUpSliceReducer,
} from '@client/market-app/sign-ups';

import {
  manageUserSliceReducer,
  MANAGE_USERS_KEY,
} from '@client/market-app/manage-users';

import {
  signOutUserSliceReducer,
  SIGNOUT_USER_KEY,
} from 'libs/market-app/sign-outs/src/index';

import {
  CREATE_LISTINGS_KEY,
  createListingSliceReducer,
} from 'libs/market-app/create-listing/src/index';

import { combineReducers } from '@reduxjs/toolkit';

import { persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

const persistConfig = {
  key: 'root',
  storage,
  whitelist: [SIGNIN_USER_KEY],
};

const combinedReducer = combineReducers({
  [SIGNIN_USER_KEY]: signInSliceReducer,
  [SIGNUP_USER_KEY]: signUpSliceReducer,
  [MANAGE_USERS_KEY]: manageUserSliceReducer,
  [SIGNOUT_USER_KEY]: signOutUserSliceReducer,
  [CREATE_LISTINGS_KEY]: createListingSliceReducer,
});

const rootReducer = (state, action) => {
  if (action.type === 'malliva/logout/fulfilled') {
    state = undefined;
  }
  return combinedReducer(state, action);
};

export default persistReducer(persistConfig, rootReducer);
