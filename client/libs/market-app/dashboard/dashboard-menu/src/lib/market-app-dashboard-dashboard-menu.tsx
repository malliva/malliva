import React, { Fragment, useEffect } from 'react';
import { MarketAppTopMenu } from '@client/market-app/top-menu';
import {
  ChatAltIcon,
  CodeIcon,
  DotsVerticalIcon,
  EyeIcon,
  FlagIcon,
  PlusIcon,
  SearchIcon,
  ShareIcon,
  StarIcon,
  ThumbUpIcon,
  AtSymbolIcon,
} from '@heroicons/react/solid';
import {
  BellIcon,
  FireIcon,
  HomeIcon,
  MenuIcon,
  TrendingUpIcon,
  UserGroupIcon,
  ChartPieIcon,
  PresentationChartLineIcon,
  AdjustmentsIcon,
  PuzzleIcon,
  TemplateIcon,
  InboxIcon,
  CreditCardIcon,
  XIcon,
  DocumentDuplicateIcon,
  CogIcon,
  ChevronDownIcon,
  ChevronUpIcon,
} from '@heroicons/react/outline';

import { Menu, Popover, Transition } from '@headlessui/react';
import { Link, Route, useHistory, useRouteMatch } from 'react-router-dom';
import { useState } from 'react';

const user = {
  name: 'Chelsea Hagon',
  email: 'chelseahagon@example.com',
  imageUrl:
    'https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
};
const navigation = [
  { name: 'Home', href: '/dashboard', icon: HomeIcon, current: true },
  {
    name: 'General',
    href: '/dashboard',
    changeType: 'hidden',
    icon: AdjustmentsIcon,
    current: false,
    submenu: [
      {
        name: 'Essentials',
        current: false,
        link: '/item-id',
      },
      {
        name: 'Domain',
        current: false,
        link: '#',
      },
      {
        name: 'Privacy',
        current: false,
        link: '#',
      },
      {
        name: 'Admin notifications',
        current: false,
        link: '#',
      },
    ],
  },
  {
    name: 'Design',
    href: '#',
    icon: TemplateIcon,
    current: false,
    changeType: 'hidden',
    submenu: [
      {
        name: 'Logos & Colors',
        current: false,
        link: '/item-id',
      },
      {
        name: 'Cover Photo',
        current: false,
        link: '#',
      },
      {
        name: 'Landing page',
        current: false,
        link: '#',
      },
      {
        name: 'Top bar',
        current: false,
        link: '#',
      },
      {
        name: 'Footer',
        current: false,
        link: '#',
      },
    ],
  },
];

const navigationTwo = [
  {
    name: 'Users',
    href: '/dashboard',
    icon: UserGroupIcon,
    current: false,
    changeType: 'hidden',
    submenu: [
      {
        name: 'Manage users',
        current: false,
        link: '/dashboard/manage-users',
      },
      {
        name: 'User rights',
        current: false,
        link: '#',
      },
      {
        name: 'View invitations',
        current: false,
        link: '#',
      },
      {
        name: 'Signup & Login',
        current: false,
        link: '#',
      },
    ],
  },
  {
    name: 'Listings',
    href: '#',
    icon: DocumentDuplicateIcon,
    current: false,
    changeType: 'hidden',
    submenu: [
      {
        name: 'Manage listings',
        current: false,
        link: '#',
      },
      {
        name: 'Categories',
        current: false,
        link: '#',
      },
      {
        name: 'Order Types',
        current: false,
        link: '#',
      },
      {
        name: 'Listings Approvals',
        current: false,
        link: '#',
      },
    ],
  },
  {
    name: 'Transaction and Reviews',
    href: '#',
    icon: UserGroupIcon,
    current: false,
  },
];
const navigationThree = [
  { name: 'Payment system', href: '#', icon: CreditCardIcon, current: false },
  {
    name: 'Email',
    href: '#',
    icon: InboxIcon,
    current: false,
    changeType: 'hidden',
    //submenu: [],
  },
  {
    name: 'Social media',
    href: '#',
    icon: AtSymbolIcon,
    current: false,
    changeType: 'hidden',
  },
  { name: 'SEO', href: '#', icon: PresentationChartLineIcon, current: false },
  { name: 'Analytics', href: '#', icon: ChartPieIcon, current: false },
  { name: 'Advanced', href: '#', icon: CogIcon, current: false },
];

import './market-app-dashboard-dashboard-menu.module.scss';

/* eslint-disable-next-line */
export interface MarketAppDashboardDashboardMenuProps {}

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}

export function MarketAppDashboardDashboardMenu(
  props: MarketAppDashboardDashboardMenuProps
) {
  const [menuObject, setMenuObject] = useState({
    index: 0,
    item: null,
  });
  const [triggerEff, setTriggerEff] = useState(false);

  const location = useHistory();

  const handleToggleSubMenu = (event, index, item) => {
    event.preventDefault();
    setMenuObject({ index, item });
    setTriggerEff(true);
  };

  const goTo = (event, subItem) => {
    event.preventDefault();
    subItem.current = true;
    debugger;
    location.push(subItem.link);
  };

  useEffect(() => {
    if (triggerEff) {
      const { item } = menuObject;
      if (item.changeType === 'hidden') {
        item.changeType = 'block';
      } else {
        item.changeType = 'hidden';
      }
      setTriggerEff(false);
    }
  }, [menuObject, triggerEff]);

  return (
    <div className="hidden lg:block lg:col-span-3 xl:col-span-3">
      <nav
        aria-label="Sidebar"
        className="sticky top-4 divide-y divide-gray-300"
      >
        <div className="pb-4 space-y-1">
          {navigation.map((item, index) => (
            <div
              key={item.name}
              onClick={($event) => handleToggleSubMenu($event, index, item)}
              aria-current={item.current ? 'page' : undefined}
            >
              <Link
                to={item.href}
                className={classNames(
                  item.current
                    ? 'bg-gray-200 text-gray-900'
                    : 'text-gray-600 hover:bg-gray-50',
                  'group flex items-center px-3 py-2 text-sm font-medium rounded-md'
                )}
              >
                <item.icon
                  className={classNames(
                    item.current
                      ? 'text-gray-500'
                      : 'text-gray-400 group-hover:text-gray-500',
                    'flex-shrink-0 -ml-1 mr-3 h-6 w-6'
                  )}
                  aria-hidden="true"
                />
                <span className="truncate" id={item.name}>
                  {item.name}
                </span>
                {item['submenu'] !== undefined &&
                item.changeType === 'hidden' && (
                  <span className="pl-2">
                    <ChevronUpIcon
                      className="self-center flex-shrink-0 h-4 w-4 text-green-500"
                      aria-hidden="true"
                    />
                  </span>
                ) ? (
                  <span className="pl-2">
                    <ChevronDownIcon
                      className="self-center flex-shrink-0 h-5 w-5 text-green-500"
                      aria-hidden="true"
                    />
                  </span>
                ) : (
                  item.changeType === 'block' &&
                  item['submenu'] !== undefined && (
                    <span className="pl-2">
                      <ChevronUpIcon
                        className="self-center flex-shrink-0 h-5 w-5 text-green-500"
                        aria-hidden="true"
                      />
                    </span>
                  )
                )}
              </Link>
              <div className={classNames(`${item.changeType} pl-8`)}>
                {item['submenu'] &&
                  item['submenu'].map((subMenu) => {
                    return (
                      <div
                        onClick={($event) => goTo($event, subMenu)}
                        key={subMenu.name}
                        className={classNames(
                          item.current
                            ? 'bg-gray-200 text-gray-900'
                            : 'text-gray-500 hover:bg-gray-50',
                          'group flex items-center px-3 py-2 text-sm font-medium rounded-md'
                        )}
                      >
                        {subMenu.name}
                      </div>
                    );
                  })}
              </div>
            </div>
          ))}
        </div>

        <div className="pb-4 pt-4 space-y-1">
          {navigationTwo.map((item, index) => (
            <div
              key={item.name}
              onClick={($event) => handleToggleSubMenu($event, index, item)}
              aria-current={item.current ? 'page' : undefined}
            >
              <div
                className={classNames(
                  item.current
                    ? 'bg-gray-200 text-gray-900'
                    : 'text-gray-600 hover:bg-gray-50',
                  'group flex items-center px-3 py-2 text-sm font-medium rounded-md'
                )}
              >
                <item.icon
                  className={classNames(
                    item.current
                      ? 'text-gray-500'
                      : 'text-gray-400 group-hover:text-gray-500',
                    'flex-shrink-0 -ml-1 mr-3 h-6 w-6'
                  )}
                  aria-hidden="true"
                />
                <span className="truncate" id={item.name}>
                  {item.name}
                </span>
                {item['submenu'] !== undefined &&
                item.changeType === 'hidden' && (
                  <span className="pl-2">
                    <ChevronUpIcon
                      className="self-center flex-shrink-0 h-4 w-4 text-green-500"
                      aria-hidden="true"
                    />
                  </span>
                ) ? (
                  <span className="pl-2">
                    <ChevronDownIcon
                      className="self-center flex-shrink-0 h-5 w-5 text-green-500"
                      aria-hidden="true"
                    />
                  </span>
                ) : (
                  item.changeType === 'block' &&
                  item['submenu'] !== undefined && (
                    <span className="pl-2">
                      <ChevronUpIcon
                        className="self-center flex-shrink-0 h-5 w-5 text-green-500"
                        aria-hidden="true"
                      />
                    </span>
                  )
                )}
              </div>
              <div className={classNames(`${item.changeType} pl-8`)}>
                {item['submenu'] &&
                  item['submenu'].map((subMenu) => {
                    return (
                      <div
                        onClick={($event) => goTo($event, subMenu)}
                        key={subMenu.name}
                        className={classNames(
                          item.current
                            ? 'bg-gray-200 text-gray-900'
                            : 'text-gray-500 hover:bg-gray-50',
                          'group flex items-center px-3 py-2 text-sm font-medium rounded-md'
                        )}
                      >
                        {subMenu.name}
                      </div>
                    );
                  })}
              </div>
            </div>
          ))}
        </div>

        <div className="pb-4 pt-4 space-y-1">
          {navigationThree.map((item, index) => (
            <div
              key={item.name}
              onClick={($event) => handleToggleSubMenu($event, index, item)}
              aria-current={item.current ? 'page' : undefined}
            >
              <div
                className={classNames(
                  item.current
                    ? 'bg-gray-200 text-gray-900'
                    : 'text-gray-600 hover:bg-gray-50',
                  'group flex items-center px-3 py-2 text-sm font-medium rounded-md'
                )}
              >
                <item.icon
                  className={classNames(
                    item.current
                      ? 'text-gray-500'
                      : 'text-gray-400 group-hover:text-gray-500',
                    'flex-shrink-0 -ml-1 mr-3 h-6 w-6'
                  )}
                  aria-hidden="true"
                />
                <span className="truncate" id={item.name}>
                  {item.name}
                </span>
                {item['submenu'] !== undefined &&
                item.changeType === 'hidden' && (
                  <span className="pl-2">
                    <ChevronUpIcon
                      className="self-center flex-shrink-0 h-4 w-4 text-green-500"
                      aria-hidden="true"
                    />
                  </span>
                ) ? (
                  <span className="pl-2">
                    <ChevronDownIcon
                      className="self-center flex-shrink-0 h-5 w-5 text-green-500"
                      aria-hidden="true"
                    />
                  </span>
                ) : (
                  item.changeType === 'block' &&
                  item['submenu'] !== undefined && (
                    <span className="pl-2">
                      <ChevronUpIcon
                        className="self-center flex-shrink-0 h-5 w-5 text-green-500"
                        aria-hidden="true"
                      />
                    </span>
                  )
                )}
              </div>
              <div className={classNames(`${item.changeType} pl-8`)}>
                {item['submenu'] &&
                  item['submenu'].map((subMenu) => {
                    return (
                      <div
                        onClick={($event) => goTo($event, subMenu)}
                        key={subMenu.name}
                        className={classNames(
                          item.current
                            ? 'bg-gray-200 text-gray-900'
                            : 'text-gray-500 hover:bg-gray-50',
                          'group flex items-center px-3 py-2 text-sm font-medium rounded-md'
                        )}
                      >
                        {subMenu.name}
                      </div>
                    );
                  })}
              </div>
            </div>
          ))}
        </div>
      </nav>
    </div>
  );
}

export default MarketAppDashboardDashboardMenu;
