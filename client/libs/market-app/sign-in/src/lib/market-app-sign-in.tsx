import {
  getSingInUser,
  setCookieForUsersPageTheme,
} from '@client/shared/account-syn-api';
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';

import { MarketAppToast } from 'libs/market-app/toast/src/index';

import './market-app-sign-in.module.scss';
import { selectSignInStateLoaded } from './market-app-sign-in.slice';

/* eslint-disable-next-line */
export interface MarketAppSignInProps {}

export function MarketAppSignIn(props: MarketAppSignInProps) {
  const dispatch = useDispatch();
  const signInDetailsLoaded = useSelector(selectSignInStateLoaded);
  const location = useHistory();
  const [login, setLogin] = useState({
    email: '',
    password: '',
  });

  const [toastMessage, setToastMessage] = useState({
    toast: [],
    showToast: false,
  });

  const handleUserLogin = (event) => {
    event.preventDefault();
    dispatch(getSingInUser(login));
  };

  useEffect(() => {
    const { loading, response } = signInDetailsLoaded;
    if (loading === 'succeeded') {
      setCookieForUsersPageTheme('create', 'jwt', JSON.stringify(response));
      location.push('/');
    } else if (loading === 'failed') {
      const { error } = signInDetailsLoaded;
      setToastMessage({ toast: error, showToast: true });
      location.push('/sign-in');
    }
  }, [location, signInDetailsLoaded]);

  const handleUserChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;

    setLogin((prevalue) => {
      return {
        ...prevalue, // Spread Operator
        [name]: value,
      };
    });
  };
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <MarketAppToast message={toastMessage} />
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <img
          className="mx-auto h-12 w-auto"
          src="https://tailwindui.com/img/logos/workflow-mark-teal-200-cyan-400.svg"
          alt="Workflow"
        />
        <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Sign in to your account
        </h2>
        <p className="mt-2 text-center text-sm text-gray-600">
          Or{' '}
          <a
            href="#"
            className="font-medium text-gray-600 hover:text-indigo-500"
          >
            start your 14-day free trial
          </a>
        </p>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <form className="space-y-6" action="#" method="POST">
            <div>
              <label
                htmlFor="email"
                className="block text-sm font-medium text-gray-700"
              >
                Email address
              </label>
              <div className="mt-1">
                <input
                  onChange={handleUserChange}
                  id="email"
                  name="email"
                  type="email"
                  autoComplete="email"
                  required
                  className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                />
              </div>
            </div>

            <div>
              <label
                htmlFor="password"
                className="block text-sm font-medium text-gray-700"
              >
                Password
              </label>
              <div className="mt-1">
                <input
                  onChange={handleUserChange}
                  id="password"
                  name="password"
                  type="password"
                  autoComplete="current-password"
                  required
                  className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                />
              </div>
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center">
                <a
                  href="/sign-up"
                  className="font-medium text-gray-600 hover:text-indigo-500"
                >
                  New to this app?
                </a>
              </div>

              <div className="text-sm">
                <a
                  href="#"
                  className="font-medium text-gray-600 hover:text-indigo-500"
                >
                  Forgot your password?
                </a>
              </div>
            </div>

            <div>
              <button
                onClick={handleUserLogin}
                type="button"
                className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Sign in
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default MarketAppSignIn;
