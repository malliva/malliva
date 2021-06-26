import React, { useEffect } from 'react';
import { useState } from 'react';
import { Switch } from '@headlessui/react';
import './market-app-sign-ups.module.scss';
import { useDispatch, useSelector } from 'react-redux';

import { postSignUpUser } from '@client/shared/account-syn-api';
import { selectSignUpStateLoaded } from './market-app-sign-ups.slice';
import { useHistory } from 'react-router-dom';
import { MarketAppToast } from 'libs/market-app/toast/src/index';

import { strict } from 'node:assert';
function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}

/* eslint-disable-next-line */
export interface MarketAppSignUpsProps {}

export function MarketAppSignUps(props: MarketAppSignUpsProps) {
  const dispatch = useDispatch();
  const location = useHistory();

  const signUpDetailsLoaded = useSelector(selectSignUpStateLoaded);
  const [terms_of_service_accepted, setEnabled] = useState(false);
  const [toastMessage, setToastMessage] = useState({
    toast: [],
    showToast: false,
  });

  const [signup, setSignUp] = useState({
    first_name: '',
    last_name: '',
    username: '',
    email: '',
    password: '',
    password_confirm: '',
  });

  useEffect(() => {
    if (signUpDetailsLoaded && signUpDetailsLoaded.loading === 'succeeded') {
      location.push('/');
    } else if (
      signUpDetailsLoaded &&
      signUpDetailsLoaded.loading === 'failed'
    ) {
      const { error } = signUpDetailsLoaded;
      setToastMessage({ toast: error, showToast: true });

      location.push('/sign-up');
    }
  }, [location, signUpDetailsLoaded]);

  const handleUserSignUp = async (event) => {
    event.preventDefault();
    const formData = {
      first_name: signup.first_name,
      last_name: signup.last_name,
      username: signup.username,
      email: signup.email,
      password: signup.password,
      password_confirm: signup.password_confirm,
      terms_of_service_accepted: terms_of_service_accepted,
    };
    dispatch(postSignUpUser(formData));
  };

  const handleUserSignUpChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;

    setSignUp((prevalue) => {
      return {
        ...prevalue, // Spread Operator
        [name]: value,
      };
    });
  };

  return (
    <div className="min-h-screen bg-white flex">
      <MarketAppToast message={toastMessage} />
      <div className="flex-1 flex flex-col justify-center py-12 px-4 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
        <div className="mx-auto w-full max-w-sm lg:w-96">
          <div>
            <img
              className="h-12 w-auto"
              src="https://tailwindui.com/img/logos/workflow-mark-teal-200-cyan-400.svg"
              alt="Workflow"
            />
            <h2 className="mt-6 text-3xl font-extrabold text-gray-900">
              Sign up to ceate an account
            </h2>
            <p className="mt-2 text-sm text-gray-600">
              Or{' '}
              <a
                href="#"
                className="font-medium text-gray-600 hover:text-indigo-500"
              >
                start your 30-day free trial
              </a>
            </p>
          </div>

          <div className="mt-8">
            <div className="mt-6">
              <form action="#" method="POST" className="space-y-6">
                <div>
                  <label
                    htmlFor="first_name"
                    className="block text-sm font-medium text-gray-700"
                  >
                    First name
                  </label>
                  <div className="mt-1">
                    <input
                      id="first_name"
                      name="first_name"
                      type="text"
                      autoComplete="text"
                      onChange={handleUserSignUpChange}
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>
                <div>
                  <label
                    htmlFor="last_name"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Last name
                  </label>
                  <div className="mt-1">
                    <input
                      onChange={handleUserSignUpChange}
                      id="last_name"
                      name="last_name"
                      type="text"
                      autoComplete="text"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>
                <div>
                  <label
                    htmlFor="username"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Username
                  </label>
                  <div className="mt-1">
                    <input
                      onChange={handleUserSignUpChange}
                      id="username"
                      name="username"
                      type="text"
                      autoComplete="text"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div>
                  <label
                    htmlFor="email"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Email address
                  </label>
                  <div className="mt-1">
                    <input
                      onChange={handleUserSignUpChange}
                      id="email"
                      name="email"
                      type="email"
                      autoComplete="email"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div className="space-y-1">
                  <label
                    htmlFor="password"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Password
                  </label>
                  <div className="mt-1">
                    <input
                      onChange={handleUserSignUpChange}
                      id="password"
                      name="password"
                      type="password"
                      autoComplete="current-password"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>
                <div className="space-y-1">
                  <label
                    htmlFor="password_confirm"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Confirm Password
                  </label>
                  <div className="mt-1">
                    <input
                      onChange={handleUserSignUpChange}
                      id="password_confirm"
                      name="password_confirm"
                      type="password"
                      autoComplete="current-password"
                      required
                      className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    />
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <div className="flex items-center">
                    <Switch.Group as="div" className="flex items-center">
                      <Switch
                        //type="terms_of_service_accepted"
                        checked={terms_of_service_accepted}
                        onChange={setEnabled}
                        className={classNames(
                          terms_of_service_accepted
                            ? 'bg-green-600'
                            : 'bg-gray-200',
                          'relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-300'
                        )}
                      >
                        <span
                          aria-hidden="true"
                          className={classNames(
                            terms_of_service_accepted
                              ? 'translate-x-5'
                              : 'translate-x-0',
                            'pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200'
                          )}
                        />
                      </Switch>
                      <Switch.Label as="span" className="ml-2">
                        <a
                          target="blank"
                          href="#"
                          className="text-xs font-medium text-gray-600"
                        >
                          Accept terms & conditions
                        </a>
                      </Switch.Label>
                    </Switch.Group>
                  </div>

                  <div className="text-sm">
                    <a
                      href="/sign-in"
                      className="font-medium text-xs text-gray-600 hover:text-indigo-500"
                    >
                      Already have an account?
                    </a>
                  </div>
                </div>

                <div>
                  <button
                    onClick={handleUserSignUp}
                    type="button"
                    className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    Sign up
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div className="hidden lg:block relative w-0 flex-1">
        <img
          className="absolute inset-0 h-full w-full object-cover"
          src="https://images.unsplash.com/photo-1505904267569-f02eaeb45a4c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80"
          alt=""
        />
      </div>
    </div>
  );
}

export default MarketAppSignUps;
